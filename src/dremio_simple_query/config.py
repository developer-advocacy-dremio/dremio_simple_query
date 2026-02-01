
import os
import yaml
from pathlib import Path
from typing import Any, Dict, Optional
from dotenv import load_dotenv

# Load .env file immediately
load_dotenv()

def load_dremio_config(profile_name: Optional[str] = None) -> Dict[str, Any]:
    """
    Load Dremio configuration from profiles.yaml or environment variables.
    
    Order of precedence:
    1. Environment Variables (override everything) - NOT fully implemented here yet, primarily for DREMIO_PROFILE selection.
    2. Selected Profile in profiles.yaml
    3. Default Profile in profiles.yaml
    
    Args:
        profile_name: Name of the profile to load. If None, checks DREMIO_PROFILE env var, then default.
    
    Returns:
        Dict suitable for passing to DremioConnection constructor.
    """
    config_dir = Path.home() / ".dremio"
    config_file = config_dir / "profiles.yaml"
    
    yaml_config = {"default_profile": None, "profiles": {}}
    
    if config_file.exists():
        try:
            with open(config_file, "r") as f:
                yaml_config = yaml.safe_load(f) or yaml_config
        except Exception as e:
            print(f"Warning: Failed to load profiles.yaml: {e}")

    # Determine profile to use
    if not profile_name:
        profile_name = os.environ.get("DREMIO_PROFILE")
    
    if not profile_name:
        profile_name = yaml_config.get("default_profile")
        
    if not profile_name:
        # Fallback to manual env vars if no profile selected
        return _load_from_env()

    # Load from YAML if profile found
    profiles = yaml_config.get("profiles", {})
    if profile_name in profiles:
        return _parse_yaml_profile(profiles[profile_name])
    
    # If profile name specified but not found in YAML, verify if it's meant to be pure env
    # For now, just return env fallback if profile missing
    print(f"Warning: Profile '{profile_name}' not found in profiles.yaml. Falling back to environment variables.")
    return _load_from_env()

def _parse_yaml_profile(profile_data: Dict[str, Any]) -> Dict[str, Any]:
    """Convert YAML profile structure to DremioConnection kwargs."""
    # Parse SSL setting (default to True)
    verify_ssl = str(profile_data.get("ssl", "true")).lower() == "true"
    
    # Derive flight URI
    base_url = profile_data.get("base_url")
    flight_uri = _derive_flight_uri(base_url)
    
    # Auto-set hostname_override for dremio.org to help with SNI
    hostname_override = None
    if flight_uri and "dremio.org" in flight_uri:
         hostname_override = "dremio.org"
         
    config = {
        "location": flight_uri,
        "base_url": base_url, # Pass explicit base_url for REST
        "project_id": profile_data.get("project_id"),
        "verify_ssl": verify_ssl,
        "hostname_override": hostname_override,
    }
    
    auth = profile_data.get("auth", {})
    auth_type = auth.get("type")
    
    if auth_type == "pat":
        config["token"] = auth.get("token")
    elif auth_type == "username_password":
        config["username"] = auth.get("username")
        config["password"] = auth.get("password")
    elif auth_type == "oauth": # Client Credentials
        config["client_id"] = auth.get("client_id")
        config["client_secret"] = auth.get("client_secret")
        config["token"] = auth.get("token") # Optional initial token
        config["scope"] = auth.get("scope")
        
    return {k: v for k, v in config.items() if v is not None}

def _derive_flight_uri(base_url: Optional[str]) -> Optional[str]:
    """Derive Flight URI from Base URL."""
    if not base_url: return None
    
    # Default to assuming base_url is the Dremio UI/API URL
    # Cloud Logic
    if "dremio.cloud" in base_url:
        host = "data.eu.dremio.cloud" if "eu.dremio.cloud" in base_url else "data.dremio.cloud"
        return f"grpc+tls://{host}:443"
        
    # Software Logic
    # Strip protocol and path
    clean = base_url.replace("https://", "").replace("http://", "").split("/")[0]
    host = clean.split(":")[0]
    
    # Heuristic: If it was https, use grpc+tls, else grpc
    scheme = "grpc+tls" if base_url.startswith("https") else "grpc"
    
    # Default Flight port for Software is 32010
    return f"{scheme}://{host}:32010"

def _load_from_env() -> Dict[str, Any]:
    """Load config purely from environment variables (legacy/manual mode)."""
    return {
        "location": os.environ.get("ARROW_ENDPOINT"),
        "token": os.environ.get("DREMIO_TOKEN") or os.environ.get("TOKEN"),
        "project_id": os.environ.get("DREMIO_PROJECT_ID"),
        # Add basic assumption for simple env usage
    }
