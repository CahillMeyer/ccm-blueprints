# /backend/app/core/config.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # This will be automatically populated from environment variables
    # e.g., 'DB_URL' from the Lambda environment settings or the .env file
    
    # We will use an in-memory store for the current prototype, 
    # but the URL remains to show production readiness.
    DATABASE_URL: str = "sqlite:///./inmemory_db.db"
    
    # Base URL for the API endpoint (e.g., used by the frontend)
    API_V1_STR: str = "/api/v1"
    
    # AWS Region for deployment (e.g., 'us-east-1')
    AWS_REGION: str = "eu-west-1" # Assuming a common deployment region

    class Config:
        env_file = ".env"

settings = Settings()
