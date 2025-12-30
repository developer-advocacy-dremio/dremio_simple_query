import pytest
import os
from dotenv import load_dotenv
from dremio_simple_query.connect import DremioConnection

import requests
import base64
from pyarrow import flight

# Load environment variables from .env file
load_dotenv()

def get_username(base_url, token):
    """
    Fetch username from Dremio REST API.
    """
    try:
        headers = {"Authorization": f"Bearer {token}"}
        r = requests.get(f"{base_url}/catalog", headers=headers)
        if r.status_code != 200:
            raise Exception(f"Failed to get catalog: {r.status_code} {r.text}")
        
        # User home container usually has the username in path
        data = r.json()
        for item in data.get("data", []):
            if item.get("containerType") == "HOME":
                # path is ["@username"]
                path = item.get("path", [])
                if path and path[0].startswith("@"):
                    return path[0][1:] # strip @
        raise Exception("Could not find HOME container with username")
    except Exception as e:
        print(f"Failed to fetch username: {e}")
        # Fallback or fail?
        # User provided token but no username. 
        # If we can't get username, we can't do Basic Auth Handshake.
        raise

def do_handshake(location, username, token):
    """
    Perform Arrow Flight Handshake to get Session Token.
    """
    client = flight.FlightClient(location=location)
    try:
        # authenticate_basic_token returns (header, value)
        auth_handler = client.authenticate_basic_token(username, token)
        val = auth_handler[1].decode('utf-8')
        # Expect "Bearer <token>"
        if val.lower().startswith("bearer "):
            return val.split(" ", 1)[1]
        else:
            # Maybe it returns just token?
            return val
    except Exception as e:
        raise Exception(f"Handshake failed: {e}")


@pytest.fixture(scope="session")
def dremio_config():
    """
    Determines the Dremio configuration based on DREMIO_PROFILE env var.
    """
    profile = os.getenv("DREMIO_PROFILE", "software")
    
    if profile == "software":
        base_url = os.getenv("DREMIO_SOFTWARE_BASE_URL")
        token = os.getenv("DREMIO_SOFTWARE_TOKEN")
        # For simple query lib, the location (arrow endpoint) is distinct from REST API base url.
        # But looking at the docs/readme, standard software arrow is grpc://<host>:32010
        # The user provided DREMIO_SOFTWARE_BASE_URL=https://v26.dremio.org/api/v3
        # We need the Arrow Flight endpoint.
        # The library expects `grpc://<host>:32010` or similar.
        # Since v26.dremio.org suggests a public/hosted testing instance or it could be a mapped domain.
        # The user didn't explicitly provide the ARROW endpoint in .env, only BASE_URL.
        # However, checking the user's .env content in the request:
        # DREMIO_SOFTWARE_BASE_URL=https://v26.dremio.org/api/v3
        # DREMIO_SOFTWARE_TOKEN=...
        
        # NOTE: Standard Dremio Arrow Flight port is 32010.
        # If DREMIO_SOFTWARE_BASE_URL is https://v26.dremio.org/api/v3, host is v26.dremio.org.
        # Let's try to derive it or default to something reasonable.
        # I'll construct it from the base URL.
        
        host = base_url.replace("https://", "").replace("http://", "").split("/")[0]
        # v26.dremio.org likely exposes 32010 for flight.
        # Using encryption defaults? 
        # The readme says:
        # Dremio Software (SSL) grpc+tls://<ip>:32010
        # Dremio Software (NoSSL) grpc://<ip>:32010
        # Since the base URL is https, I'll assume TLS for Flight too if possible, 
        # but often internal setups are mixed. Let's try grpc+tls first if https is used.
        
        scheme = "grpc+tls" if base_url.startswith("https") else "grpc"
        location = f"{scheme}://{host}:32010"
        
        # Performance Handshake to get Session Token
        print(f"Authenticating against {location}...")
        try:
            username = get_username(base_url, token)
            print(f"Derived username: {username}")
            session_token = do_handshake(location, username, token)
            print("Authentication successful.")
            effective_token = session_token
        except Exception as e:
            print(f"Auth failed, falling back to provided token: {e}")
            effective_token = token
        
        return {
            "token": effective_token,
            "location": location,
            "test_folder": os.getenv("DREMIO_SOFTWARE_TEST_FOLDER")
        }
        
    elif profile == "cloud":
        # Cloud defaults
        # data.dremio.cloud:443
        # location needs to be full string e.g. grpc+tls://data.dremio.cloud:443
        token = os.getenv("DREMIO_CLOUD_TOKEN")
        location = "grpc+tls://data.dremio.cloud:443"
        return {
            "token": token,
            "location": location,
            "project_id": os.getenv("DREMIO_CLOUD_PROJECTID"),
            "test_folder": os.getenv("DREMIO_CLOUD_TEST_FOLDER")
        }
        
    else:
        pytest.fail(f"Unknown DREMIO_PROFILE: {profile}")

@pytest.fixture(scope="session")
def dremio_client(dremio_config):
    """
    Returns a connected DremioConnection instance.
    """
    try:
        con = DremioConnection(dremio_config["token"], dremio_config["location"])
        return con
    except Exception as e:
        pytest.fail(f"Failed to initialize DremioConnection: {e}")
