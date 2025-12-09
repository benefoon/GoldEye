# src/config.py
from pydantic import BaseSettings, AnyHttpUrl, Field, validator
from typing import Optional
from pathlib import Path

class Settings(BaseSettings):
    # app
    app_env: str = Field("development", env="APP_ENV")
    app_host: str = Field("0.0.0.0", env="APP_HOST")
    app_port: int = Field(8000, env="APP_PORT")
    log_level: str = Field("INFO", env="LOG_LEVEL")

    # source
    price_source_url: Optional[AnyHttpUrl] = Field(None, env="PRICE_SOURCE_URL")
    price_source_api_key: Optional[str] = Field(None, env="PRICE_SOURCE_API_KEY")

    # db
    database_url: str = Field(..., env="DATABASE_URL")

    # telegram
    telegram_bot_token: Optional[str] = Field(None, env="TELEGRAM_BOT_TOKEN")
    telegram_chat_id: Optional[str] = Field(None, env="TELEGRAM_CHAT_ID")

    # collector tuning
    collector_interval_seconds: int = Field(60, env="COLLECTOR_INTERVAL_SECONDS")
    collector_timeout_seconds: int = Field(10, env="COLLECTOR_TIMEOUT_SECONDS")
    collector_max_backoff_seconds: int = Field(300, env="COLLECTOR_MAX_BACKOFF_SECONDS")
    price_threshold_pct: float = Field(0.5, env="PRICE_THRESHOLD_PCT")

    # misc
    sentry_dsn: Optional[str] = Field(None, env="SENTRY_DSN")

    class Config:
        env_file = ".env"
        case_sensitive = False

    @validator("price_threshold_pct")
    def threshold_must_be_positive(cls, v: float) -> float:
        if v < 0:
            raise ValueError("PRICE_THRESHOLD_PCT must be >= 0")
        return v

settings = Settings()
