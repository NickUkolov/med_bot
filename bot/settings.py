from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict

class Tg(BaseModel):
    token: str

class Pg(BaseModel):
    url: str

class Redis(BaseModel):
    url: str

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_nested_delimiter='__')

    admin: int
    tg: Tg
    pg: Pg
    redis: Redis

settings = Settings()
