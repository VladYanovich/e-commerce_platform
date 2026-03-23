from pathlib import Path
from functools import lru_cache

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class TelegramConfig(BaseModel):
    bot_token: str
    channel_id: int


class RabbitMQConfig(BaseModel):
    url: str


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )

    telegram: TelegramConfig
    rabbitmq: RabbitMQConfig


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()