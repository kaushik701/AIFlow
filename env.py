# aiflow/utils/env.py
import os
from dotenv import load_dotenv

def load_environment():
    """Load environment variables from .env file."""
    load_dotenv()
    
    # Check for required environment variables
    required_vars = ["OPENAI_API_KEY"]
    missing_vars = [var for var in required_vars if not os.environ.get(var)]
    
    if missing_vars:
        raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
        
    return {
        "openai_api_key": os.environ.get("OPENAI_API_KEY"),
        "openai_org_id": os.environ.get("OPENAI_ORG_ID"),
        "log_level": os.environ.get("LOG_LEVEL", "INFO"),
        "max_tokens_default": int(os.environ.get("MAX_TOKENS_DEFAULT", 1000)),
        "temperature_default": float(os.environ.get("TEMPERATURE_DEFAULT", 0.7)),
    }