import os
from typing import Union, Any
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path=dotenv_path)

class EnvHandler:    
    def __init__(self):
        """Add new variables below"""
        self.app = {
            "api_key": self.get("API_KEY"),
            "secret_key": self.get("SECRET_KEY"),
        }

    def get(self, key: str, default: Union[Any, None] = None, cast: Union[type, None] = None) -> any:
        """
        Fetch an environment variable with optional casting and default fallback.
        - (key) Name of the environment variable.
        - (default) Default value if the variable is not found.
        - `cast`: Type to cast the value into (e.g., int, float, bool).
        - `returns`: The value of the environment variable.
        - `raises`: `KeyError` if the variable is not found and no default is provided.
        """
        value = os.getenv(key, default)
        if value is None:
            raise KeyError(f"Missing required environment variable: {key}")        
        if cast:
            try:
                value = cast(value)
            except ValueError as e:
                raise ValueError(f"Error casting environment variable {key} to {cast}: {e}")
        
        return value
    
env = EnvHandler()