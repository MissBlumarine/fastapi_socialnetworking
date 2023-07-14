import os
from functools import lru_cache

from dotenv import load_dotenv
from pydantic import BaseSettings, SecretStr

# Load environment variables from .env file
load_dotenv()


@lru_cache()
def get_settings():
    return Settings()


class Settings(BaseSettings):
    api_debug: bool = True
    api_host: str
    api_port: str
    api_root_path: str

    db_user: str
    db_password: str
    db_host: str
    db_port: str
    db_name: str

    auth_secret_key: str
    auth_algorithm: str
    auth_access_token_expire_minutes: int

    redis_host: str
    redis_port: str
    redis_db: int
    redis_password: SecretStr

    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    class Config:
        env_file = ".env"