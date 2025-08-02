from typing import List, Union
from pydantic import AnyHttpUrl, validator
from pydantic_settings import BaseSettings
from decouple import config

class Settings(BaseSettings):
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "Healthcare Data Management"
    
    # BACKEND_CORS_ORIGINS is a comma-separated list of origins
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = [
        "http://localhost:3000",  # React frontend
    ]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # MongoDB settings
    MONGODB_URL: str = config("MONGODB_URL", default="mongodb://localhost:27017/healthcare")
    
    # JWT settings
    JWT_SECRET: str = config("JWT_SECRET", default="your-super-secret-key-here")
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # Blockchain settings
    BLOCKCHAIN_NODE_URL: str = config("BLOCKCHAIN_NODE_URL", default="http://localhost:7545")
    BLOCKCHAIN_NETWORK_ID: int = config("BLOCKCHAIN_NETWORK_ID", default=5777, cast=int)
    SMART_CONTRACT_ADDRESS: str = config(
        "SMART_CONTRACT_ADDRESS",
        default="0x0000000000000000000000000000000000000000"
    )

    model_config = {
        "case_sensitive": True,
        "env_file": ".env"
    }

settings = Settings() 