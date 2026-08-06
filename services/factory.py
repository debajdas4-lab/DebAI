"""
--------------------------------------------------------
Configuration File
Expense AI Assistant
--------------------------------------------------------
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


# ======================================================
# LLM Configuration
# ======================================================

LLM_PROVIDER = "groq"

LLM_MODEL = "groq/llama-3.3-70b-versatile"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")


# ======================================================
# Application Configuration
# ======================================================

APP_NAME = "Expense AI Assistant"

APP_VERSION = "1.0"

DEBUG = True


# ======================================================
# Upload Configuration
# ======================================================

UPLOAD_FOLDER = "uploads"

MAX_FILE_SIZE_MB = 10

SUPPORTED_FILE_TYPES = [
    ".pdf",
    ".jpg",
    ".jpeg",
    ".png"
]


# ======================================================
# AI Decision Thresholds
# ======================================================

AUTO_APPROVE_LIMIT = 5000

MANAGER_APPROVAL_LIMIT = 20000

HIGH_RISK_SCORE = 80


# ======================================================
# Logging
# ======================================================

LOG_FOLDER = "logs"

LOG_LEVEL = "INFO"


# ======================================================
# API Configuration
# ======================================================

HOST = "0.0.0.0"

PORT = 8000


# ======================================================
# Security
# ======================================================

API_SECRET = os.getenv("API_SECRET")


# ======================================================
# Database (Future)
# ======================================================

DATABASE_URL = os.getenv("DATABASE_URL")


# ======================================================
# OCR (Future)
# ======================================================

OCR_ENGINE = "tesseract"


# ======================================================
# Power Platform (Future)
# ======================================================

POWER_AUTOMATE_WEBHOOK = os.getenv("POWER_AUTOMATE_WEBHOOK")


# ======================================================
# Power BI (Future)
# ======================================================

POWERBI_WORKSPACE = os.getenv("POWERBI_WORKSPACE")