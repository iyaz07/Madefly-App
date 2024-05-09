import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the variables using os.getenv()
DB_URL = os.getenv("DB_URL")