import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    APP_NAME = os.getenv("APP_NAME", "Employee Expense Management")
    APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
    API_KEY = os.getenv("API_KEY", "local-dev-key")
    LLM_PROVIDER = os.getenv("LLM_PROVIDER", "groq")
    MODEL_NAME = os.getenv("MODEL_NAME", "groq/llama-3.3-70b-versatile")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    TEMPERATURE = float(os.getenv("TEMPERATURE", "0.2"))
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
    AUTO_APPROVAL_LIMIT = float(os.getenv("AUTO_APPROVAL_LIMIT", "5000"))
    MANAGER_APPROVAL_LIMIT = float(os.getenv("MANAGER_APPROVAL_LIMIT", "20000"))
    HIGH_RISK_SCORE = float(os.getenv("HIGH_RISK_SCORE", "80"))
    API_URL = os.getenv("EEM_API_URL", "http://localhost:8000")
