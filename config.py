import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.gettoken("BOT_TOKEN")

DB_ENGINE = os.environ.get("DB_ENGINE")
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
DB_NAME = os.environ.get("DB_NAME")
DB_IP = os.environ.get("DB_IP")

DATABASE_URL = f"{DB_ENGINE}://{DB_USER}:{DB_PASS}@{DB_IP}:{DB_PORT}/{DB_NAME}"
