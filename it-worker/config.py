import os

from dotenv import load_dotenv

APP_ENV = os.getenv("APP_ENV", "dev")

if os.path.exists(".env"):
    load_dotenv(".env")

_env_file = f".env.{APP_ENV}"
if os.path.exists(_env_file):
    load_dotenv(_env_file, override=True)

DB_HOST: str = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "pedia")

API_TOKEN = os.getenv("API_TOKEN", "")

REQUEST_TIMEOUT = float(os.getenv("REQUEST_TIMEOUT", "5"))
HTTP_PORT = int(os.getenv("HTTP_PORT", "8000"))
