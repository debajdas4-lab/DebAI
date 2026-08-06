from crewai import Task


class RiskTask:

    def task(self, agent):

        return Task(

            description="""
            Assess fraud risk and duplicate receipt possibility for employee
            {employee_id}, amount {amount}, and receipt {receipt_name}. Use
            the previous receipt and policy analyses as evidence.
            """,

            expected_output="""
            Risk assessment report.
            """,

            agent=agent
        )
