from crewai import Task


class ManagerTask:

    def task(self, agent):

        return Task(

            description="""
            Review the receipt, policy, and risk analyses and recommend:

            - Approve
            - Reject
            - Escalate
            """,

            expected_output="""
            Return JSON with decision, confidence, risk_score, and
            justification. Choose AUTO_APPROVE only when clearly compliant
            and low risk; otherwise choose MANAGER_REVIEW or REJECT.
            """,

            agent=agent
        )
