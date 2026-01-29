from typing import Optional, Union, List, Tuple, Dict
from pyarrow import flight
from pyarrow.flight import FlightClient
import duckdb
import pyarrow.dataset as ds
import polars as pl
import pandas as pd
import requests
from http.cookies import SimpleCookie

class CookieMiddleware(flight.ClientMiddleware):
    """
    Middleware that handles receiving and sending cookies.
    Parses Set-Cookie headers and maintains a cookie jar.
    """

    def __init__(self, factory):
        self.factory = factory

    def received_headers(self, headers):
        # We might receive multiple Set-Cookie headers
        # or a single one.
        for key, values in headers.items():
            if key.lower() == "set-cookie":
                for value in values:
                    # value looks like "key=value; Path=/; ..."
                    # We use SimpleCookie to parse it easily
                    try:
                        cookie = SimpleCookie()
                        cookie.load(value)
                        for name, morsel in cookie.items():
                            self.factory.cookies[name] = morsel.value
                    except Exception as e:
                        pass # Silently fail on cookie parsing

    def sending_headers(self):
        # Construct Cookie header from the jar
        if not self.factory.cookies:
            return {}
        
        cookie_string = "; ".join([f"{k}={v}" for k, v in self.factory.cookies.items()])
        return {"Cookie": cookie_string}

class CookieFactory(flight.ClientMiddlewareFactory):
    """
    Factory that creates CookieMiddleware. 
    Shared state (cookies) is maintained here.
    """

    def __init__(self):
        # Dict of cookie_name -> cookie_value
        self.cookies = {}

    def start_call(self, info):
        return CookieMiddleware(self)

class DremioConnection:
    """
    A connection to Dremio via Apache Arrow Flight.
    Supports authenticating via PAT or Username/Password (Handshake),
    and handles Dremio Cloud Project IDs via Cookies.
    """
    
    def __init__(self, 
                 location: Optional[str] = None, 
                 token: Optional[str] = None, 
                 username: Optional[str] = None, 
                 password: Optional[str] = None,
                 project_id: Optional[str] = None,
                 profile: Optional[str] = None):
        """
        Initialize the Dremio Connection.

        Args:
            location (str): The Arrow Flight endpoint (e.g., "grpc+tls://data.dremio.cloud:443").
            token (Optional[str]): A Personal Access Token (PAT).
            username (Optional[str]): Dremio username (for Basic Auth Handshake).
            password (Optional[str]): Dremio password (for Basic Auth Handshake).
            project_id (Optional[str]): Dremio Cloud Project ID.
            profile (Optional[str]): Name of the profile to use from ~/.dremio/profiles.yaml.
        
        Raises:
            ValueError: If neither token nor (username and password) are provided.
        """
        
        # If profile is specified, load details from ~/.dremio/profiles.yaml
        if profile:
            details = self._load_profile(profile)
            # Override/Set values if they weren't provided in the arguments
            if not location and details.get("location"):
                location = details["location"]
            if not token and details.get("token"):
                token = details["token"]
            if not username and details.get("username"):
                username = details["username"]
            if not password and details.get("password"):
                password = details["password"]
            if not project_id and details.get("project_id"):
                project_id = details["project_id"]

        if not location:
            raise ValueError("Must provide 'location' or a 'profile' with a valid endpoint derivation.")

        self.location = location
        self.project_id = project_id
        
        # Initialize Flight Client with Cookie Middleware
        self.cookie_factory = CookieFactory()
        
        # Inject project_id as a cookie if provided
        # This is required for Dremio Cloud to switch context to non-default projects
        if self.project_id:
            self.cookie_factory.cookies['project_id'] = self.project_id
            
        self.client = FlightClient(location=(location), middleware=[self.cookie_factory])
        
        # Authentication Logic
        self.token = token
        
        if not self.token and (username and password):
            # Perform Handshake to get session token
            try:
                options, token_pair = self.client.authenticate_basic_token(username, password)
                if token_pair:
                    self.token = token_pair.decode("utf-8") if isinstance(token_pair, bytes) else str(token_pair)
            except Exception as e:
                raise ConnectionError(f"Failed to authenticate with username/password: {e}")
        
        if not self.token:
            raise ValueError("Must provide either 'token' or 'username' and 'password' (directly or via profile).")

        # Construct Headers
        self.headers = [
            (b"authorization", f"Bearer {self.token}".encode("utf-8"))
        ]

    def _load_profile(self, profile_name: str) -> dict:
        """
        Load profile configuration from ~/.dremio/profiles.yaml.
        
        Args:
            profile_name (str): The name of the profile to load.
            
        Returns:
            dict: Dictionary containing connection details (location, token/user/pass, project_id).
        """
        import os
        import yaml
        
        home = os.path.expanduser("~")
        profile_path = os.path.join(home, ".dremio", "profiles.yaml")
        
        if not os.path.exists(profile_path):
            raise FileNotFoundError(f"Profile config not found at {profile_path}")
            
        try:
            with open(profile_path, 'r') as f:
                config = yaml.safe_load(f)
        except Exception as e:
            raise ValueError(f"Failed to parse {profile_path}: {e}")
            
        profiles = config.get("profiles", {})
        
        # Handle 'default_profile' if implied or explicitly requested
        if profile_name == "default" and "default_profile" in config:
             profile_name = config["default_profile"]
             
        if profile_name not in profiles:
             raise ValueError(f"Profile '{profile_name}' not found in {profile_path}")
             
        profile_data = profiles[profile_name]
        return self._derive_connection_details(profile_data)

    def _derive_connection_details(self, profile_data: dict) -> dict:
        """
        Derive DremioConnection arguments from raw profile data.
        
        Args:
            profile_data (dict): The raw dictionary from the yaml profile.
            
        Returns:
            dict: A dictionary with keys: location, token, username, password, project_id.
        """
        details = {}
        
        # 1. Extract Project ID, Username, Password, Token
        details["project_id"] = profile_data.get("project_id")
        
        auth = profile_data.get("auth", {})
        auth_type = auth.get("type")
        
        if auth_type == "pat":
            details["token"] = auth.get("token")
        elif auth_type == "username_password":
            details["username"] = auth.get("username")
            details["password"] = auth.get("password")
            
        # 2. Derive Location (Arrow Flight Endpoint)
        base_url = profile_data.get("base_url", "")
        is_ssl = str(profile_data.get("ssl", "true")).lower() == "true"
        
        # Derive scheme
        scheme = "grpc+tls" if is_ssl else "grpc"
        
        # Derive host and port
        if "api.dremio.cloud" in base_url or "data.dremio.cloud" in base_url:
            # Cloud
            if "eu.dremio.cloud" in base_url:
                 # EU Cloud
                 host = "data.eu.dremio.cloud"
            else:
                 # NA Cloud
                 host = "data.dremio.cloud"
            port = "443"
        else:
             # Software
             # Remove http:// or https://
             clean_url = base_url.replace("https://", "").replace("http://", "")
             # Split off path if present
             clean_url = clean_url.split("/")[0]
             # Check for port in URL
             if ":" in clean_url:
                 host = clean_url.split(":")[0]
                 # We ignore the REST port (9047) and assume Flight port 32010
                 # If user wants custom flight port, they might need to be more explicit,
                 # but for now we follow the simple request logic.
             else:
                 host = clean_url
            
             port = "32010"
             
        details["location"] = f"{scheme}://{host}:{port}"
        
        return details
        
    def query(self, query: str) -> flight.FlightStreamReader:
        """
        Execute a SQL query against Dremio.

        Args:
            query (str): The SQL query string.

        Returns:
            flight.FlightStreamReader: The stream reader for the result set.
        """
        ## Options for Query
        # Note: Dremio Flight might expect project_id in properties or headers.
        # We send in headers primarily, but some clients use properties.
        # However, standard gRPC headers are usually what counts.
        options = flight.FlightCallOptions(headers=self.headers)
        
        ## Get ticket to for query execution, used to get results
        flight_info = self.client.get_flight_info(flight.FlightDescriptor.for_command(query), options)
    
        ## Get Results (Return Value a FlightStreamReader)
        results = self.client.do_get(flight_info.endpoints[0].ticket, options)
        return results
        
    def toArrow(self, query: str) -> flight.FlightStreamReader:
        """Execute query and return Arrow Flight Stream Reader."""
        return self.query(query)
    
    def toDuckDB(self, querystring: str) -> duckdb.DuckDBPyRelation:
        """Execute query and return DuckDB Relation."""
        streamReader = self.query(querystring)
        table = streamReader.read_all()
        my_ds = ds.dataset(source=[table])
        return duckdb.arrow(my_ds)
    
    def toPolars(self, querystring: str) -> pl.DataFrame:
        """Execute query and return Polars DataFrame."""
        streamReader = self.query(querystring)
        table = streamReader.read_all()
        # Polars from_arrow expects a Table or RecordBatch
        df = pl.from_arrow(table)
        return df

    def toPandas(self, querystring: str) -> pd.DataFrame:
        """Execute query and return Pandas DataFrame."""
        streamReader = self.query(querystring)
        df = streamReader.read_pandas()
        return df
    
## Function to Retrieve PAT TOken from Dremio
def get_token(uri: str, payload: Dict[str, str]) -> str:
    """
    Retrieve authentication token from Dremio REST API.
    
    Args:
        uri (str): Login endpoint URI.
        payload (dict): JSON payload with username and password.
        
    Returns:
        str: The authentication token.
    """
    # Make the POST request
    response = requests.post(uri, json=payload)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        # Extract the token
        return data.get("token", "")
    else:
        print("Failed to get a valid response. Status code:", response.status_code)
        return ""
