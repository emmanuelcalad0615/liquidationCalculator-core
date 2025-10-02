from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Setting()
