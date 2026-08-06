from crewai import Agent
from agents.base_llm import get_llm


class PolicyAgent:

    def agent(self):

        return Agent(

            role="Expense Policy Specialist",

            goal="Verify compliance with corporate expense policy.",

            backstory="""
            Expert in travel, hotel,
            meal and reimbursement policies.
            """,

            llm=get_llm(),

            verbose=True
        )