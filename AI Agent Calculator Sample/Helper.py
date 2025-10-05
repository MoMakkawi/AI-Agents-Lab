# Load environment variables
from dotenv import load_dotenv
from pathlib import Path
import os

def try_configure():
    # Always load .env from the same folder as main.py
    env_path = Path(__file__).resolve().parent / ".env"
    load_dotenv(env_path)

    huggingface_token = os.getenv("HUGGINGFACE_TOKEN")

    if not huggingface_token:
        raise ValueError("HUGGINGFACE_TOKEN is not set")
