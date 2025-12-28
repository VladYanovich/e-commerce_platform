from pydantic import BaseModel
from pydantic import PostgresDsn
from pydantic_settings import BaseSettings

class RunConfig(BaseModel):
    host: str = "127.0.0.1"
    port: int = 8080

class ApiPrefix(BaseModel):
    prefix: str = "/products"

class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False,
    echo_pool: bool = False,
    pool_size: int = 50,
    max_overflow: int = 10

class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: ApiPrefix = ApiPrefix()
    db: DatabaseConfig

settings: Settings = Settings()
