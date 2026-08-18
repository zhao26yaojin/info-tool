import logging
import os
from datetime import datetime

from dotenv import load_dotenv

APP_ENV = os.getenv("APP_ENV", "dev")

_env_file = f".env.{APP_ENV}"
if os.path.exists(_env_file):
    load_dotenv(_env_file)

DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", "3306"))
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "pedia")

API_TOKEN = os.getenv("API_TOKEN", "")

REQUEST_TIMEOUT = float(os.getenv("REQUEST_TIMEOUT", "10"))
HTTP_PORT = int(os.getenv("HTTP_PORT", "8000"))


def setup_logging():
    logging.basicConfig(
        level=os.getenv("LOG_LEVEL", "INFO"),
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )


def current_season_year():
    """欧洲足球赛季通常跨两个自然年、以开赛年份命名（如 2026 指 2026/2027 赛季），这里按 7 月为分界估算。"""
    now = datetime.now()
    return now.year if now.month >= 7 else now.year - 1
