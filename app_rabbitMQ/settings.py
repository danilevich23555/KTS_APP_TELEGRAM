import os
from pydantic import BaseSettings
from dotenv import load_dotenv


load_dotenv()

class Settings(BaseSettings):



    rabbit_dsn: str = os.getenv('RABBITMQ_DSN', '')
    rabbit_user: str = os.getenv('RABBITMQ_USER', '')
    rabbit_password: str = os.getenv('RABBITMQ_PASS', '')

    class Config:
        env_file = ".env"
        env_file_encoding = 'utf-8'


settings = Settings()
