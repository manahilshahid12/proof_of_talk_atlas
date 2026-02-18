import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

if not HF_API_KEY:
    raise ValueError("Hugging Face API key not found.")

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
SUMMARY_MODEL = "facebook/bart-large-cnn"

