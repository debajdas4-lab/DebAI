from crewai import Agent
from agents.base_llm import get_llm


class EmployeeAgent:

    def agent(self):

        return Agent(

            role="Employee Guidance Specialist",

            goal="Provide friendly feedback to employees.",

            backstory="""
            HR and finance communication expert.
            """,

            llm=get_llm(),

            verbose=True
        )