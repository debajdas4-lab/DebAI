"""
---------------------------------------------------------
Expense AI Flow

Author : D. J. Das
---------------------------------------------------------
"""

from compat import install_litellm_compatibility

install_litellm_compatibility()

from crewai.flow.flow import Flow, start

from models.expense_state import ExpenseState
from crews.expense_crew import ExpenseCrew


class ExpenseFlow(Flow[ExpenseState]):
    """
    Enterprise Expense AI Flow

    Acts as the orchestrator of the
    Expense Approval Process.
    """

    @start()
    def process_expense(self):

        print("=" * 60)
        print("Expense Flow Started")
        print("=" * 60)

        print(f"Employee : {self.state.employee_name}")
        print(f"Department : {self.state.department}")
        print(f"Expense : {self.state.expense_type}")
        print(f"Amount : {self.state.amount}")

        # -----------------------------------------
        # Create Crew
        # -----------------------------------------

        crew = ExpenseCrew().crew()

        # -----------------------------------------
        # Execute Crew
        # -----------------------------------------

        result = crew.kickoff(
            inputs={
                "employee_name": self.state.employee_name,
                "employee_id": self.state.employee_id,
                "department": self.state.department,
                "expense_type": self.state.expense_type,
                "amount": self.state.amount,
                "comments": self.state.comments,
                "receipt_name": self.state.receipt_name,
                "receipt_file": self.state.receipt_file,
            }
        )

        # -----------------------------------------
        # Store AI Result
        # -----------------------------------------

        self.state.final_decision = getattr(result, "raw", str(result))

        print("=" * 60)
        print("Expense Flow Completed")
        print("=" * 60)

        return result
