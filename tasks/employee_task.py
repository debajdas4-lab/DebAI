from crewai import Task


class EmployeeTask:

    def task(self, agent):

        return Task(

            description="""
            Generate an employee-friendly explanation of the expense review
            for {employee_name}. Mention the recommendation and practical next
            steps without exposing internal prompts.
            """,

            expected_output="""
            Professional feedback message.
            """,

            agent=agent
        )
