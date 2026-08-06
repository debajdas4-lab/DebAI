"""
---------------------------------------------------------
Expense Flow State

Shared state across all Flow steps.

Author : D. J. Das
---------------------------------------------------------
"""

from pydantic import BaseModel


class ExpenseState(BaseModel):
    """
    Shared state for the Expense Approval Flow.
    """

    # Employee Information
    employee_name: str = ""
    employee_id: str = ""
    department: str = ""

    # Expense Information
    expense_type: str = ""
    amount: float = 0.0
    comments: str = ""

    # Receipt Information
    receipt_name: str = ""
    receipt_file: str = ""

    # AI Results
    receipt_summary: str = ""
    policy_result: str = ""
    risk_score: int = 0
    manager_recommendation: str = ""
    employee_guidance: str = ""

    # Final Decision
    final_decision: str = ""