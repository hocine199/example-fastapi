from pydantic_settings import BaseSettings, SettingsConfigDict
import os

class Settings(BaseSettings): 
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithm: str
    access_token_expire_time: int

    model_config = SettingsConfigDict(env_file=".env")
    # class Config:
    #         env_file = f"{os.path.dirname(os.path.abspath(__file__))}/../.env"


settings = Settings()