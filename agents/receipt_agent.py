from crewai import Agent

from agents.base_llm import get_llm


class ReceiptAgent:

    def agent(self):

        return Agent(

            role="Receipt Analysis Specialist",

            goal="Extract and validate information from employee expense receipts.",

            backstory="""
            You are an expert financial document analyst.
            Your responsibility is to accurately extract
            vendor, amount, taxes, currency, invoice number,
            and receipt validity.
            """,

            llm=get_llm(),

            verbose=True
        )