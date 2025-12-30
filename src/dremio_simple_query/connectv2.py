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
                 location: str, 
                 token: Optional[str] = None, 
                 username: Optional[str] = None, 
                 password: Optional[str] = None,
                 project_id: Optional[str] = None):
        """
        Initialize the Dremio Connection.

        Args:
            location (str): The Arrow Flight endpoint (e.g., "grpc+tls://data.dremio.cloud:443").
            token (Optional[str]): A Personal Access Token (PAT).
            username (Optional[str]): Dremio username (for Basic Auth Handshake).
            password (Optional[str]): Dremio password (for Basic Auth Handshake).
            project_id (Optional[str]): Dremio Cloud Project ID.
        
        Raises:
            ValueError: If neither token nor (username and password) are provided.
        """
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
            raise ValueError("Must provide either 'token' or 'username' and 'password'.")

        # Construct Headers
        self.headers = [
            (b"authorization", f"Bearer {self.token}".encode("utf-8"))
        ]
        
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
