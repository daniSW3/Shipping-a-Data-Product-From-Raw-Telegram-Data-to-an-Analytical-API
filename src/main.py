# src/main.py
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Access environment variables
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Test printing (for debugging)
print(f"Bot Token: {TELEGRAM_BOT_TOKEN}")
print(f"Database: {DB_NAME}@{DB_HOST}:{DB_PORT}")