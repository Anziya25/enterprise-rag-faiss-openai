import os
from dotenv import load_dotenv

# Read the .env file
load_dotenv()

# Get values from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

LLM_MODEL = os.getenv("LLM_MODEL")

EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

CHUNK_SIZE = int(os.getenv("CHUNK_SIZE"))

CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP"))

VECTOR_STORE_PATH = os.getenv("VECTOR_STORE_PATH")

UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")