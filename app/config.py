import os
from dotenv import load_dotenv


SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = "HS256"

DATABASE_URL = os.getenv("DATABASE_URL")
