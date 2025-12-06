from pydantic import BaseSettings, AnyHttpUrl, Field
from typing import Optional


class Settings(BaseSettings):
# App
app_env: str = Field('development', env='APP_ENV')
host: str = Field('0.0.0.0', env='APP_HOST')
port: int = Field(8000, env='APP_PORT')
log_level: str = Field('INFO', env='LOG_LEVEL')


# Data source
price_source_url: Optional[AnyHttpUrl] = Field(None, env='PRICE_SOURCE_URL')
price_source_api_key: Optional[str] = Field(None, env='PRICE_SOURCE_API_KEY')


# DB
database_url: str = Field(..., env='DATABASE_URL')


# Telegram
telegram_bot_token: Optional[str] = Field(None, env='TELEGRAM_BOT_TOKEN')
telegram_chat_id: Optional[str] = Field(None, env='TELEGRAM_CHAT_ID')


# Collector tuning
collector_interval_seconds: int = Field(60, env='COLLECTOR_INTERVAL_SECONDS')
collector_timeout_seconds: int = Field(10, env='COLLECTOR_TIMEOUT_SECONDS')


class Config:
env_file = '.env'
case_sensitive = False


settings = Settings()
