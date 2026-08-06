
from crewai import Agent

from agents.base_llm import get_llm

class ManagerAgent:

    def agent(self):

        return Agent(

            role="Approval Recommendation Specialist",

            goal="Recommend Approve, Reject or Escalate.",

            backstory="""
            Senior finance manager with
            expertise in corporate expense approval.
            """,

            llm=get_llm(),

            verbose=True
        )