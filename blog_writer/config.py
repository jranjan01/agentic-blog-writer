import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL")
GEMENI_LITE_MODEL = os.getenv("GEMENI_LITE_MODEL")
