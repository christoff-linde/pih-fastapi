"""The settings module for the FastAPI application."""

from typing import Optional
from functools import lru_cache
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_env: str = "local"
    db_engine: Optional[str] = "postgresql"
    db_host: Optional[str] = "pih-fastapi-db"
    db_port: Optional[str] = "5498"
    db_user: Optional[str] = "pih"
    db_password: Optional[str] = "pih"
    log_sql_statements: bool = True

    @property
    def database_url(self) -> str:
        return f"{self.db_engine}://{self.db_user}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"


@lru_cache
def get_settings() -> Settings:
    return Settings()
