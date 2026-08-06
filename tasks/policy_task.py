from crewai import Task


class PolicyTask:

    def task(self, agent):

        return Task(

            description="""
            Verify whether {employee_name}'s {expense_type} expense of
            {amount} in department {department} complies with company policy.
            Use the receipt analysis from the previous task.
            """,

            expected_output="""
            Compliance Report.
            """,

            agent=agent
        )
