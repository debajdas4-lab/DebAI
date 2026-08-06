from crewai import Agent
from agents.base_llm import get_llm


class RiskAgent:

    def agent(self):

        return Agent(

            role="Fraud Detection Specialist",

            goal="Identify suspicious or risky expense claims.",

            backstory="""
            Expert in duplicate receipts,
            fraudulent claims,
            abnormal spending
            and compliance violations.
            """,

            llm=get_llm(),

            verbose=True
        )