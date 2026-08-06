from compat import install_litellm_compatibility

install_litellm_compatibility()

from crewai import LLM
from config import Config


def get_llm():
    api_key = Config.GROQ_API_KEY if Config.LLM_PROVIDER == "groq" else Config.OPENAI_API_KEY
    return LLM(model=Config.MODEL_NAME, api_key=api_key, temperature=Config.TEMPERATURE)
