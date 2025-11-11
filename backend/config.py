
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()  # carga las variables del .env

class Setting(BaseSettings):
    database_url: str
    secret_key: str
    frontend_url: str
class Setting(BaseSettings):
    database_url: str
    secret_key: str
    frontend_url: list[str]


    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Setting()
