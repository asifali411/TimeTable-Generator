from dotenv import load_dotenv
import os
from pathlib import Path

# load .env located next to this file
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

# accept common env names as fallback
SQL_DATABASE_URL = (
	os.getenv("SQL_DATABASE_URL")
	or os.getenv("DATABASE_URL")
	or os.getenv("Database_url")
)
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
