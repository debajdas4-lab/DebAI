from crewai import LLM

from config import Config


def get_llm():

    return LLM(
        model=Config.MODEL_NAME,
        api_key=Config.GROQ_API_KEY,
        temperature=Config.TEMPERATURE
    )