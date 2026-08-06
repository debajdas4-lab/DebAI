from pydantic import BaseModel

from models.receipt_result import ReceiptResult
from models.policy_result import PolicyResult
from models.risk_result import RiskResult
from models.approval_result import ApprovalResult
from models.employee_result import EmployeeResult


class ExpenseResponse(BaseModel):

    status: str

    receipt: ReceiptResult

    policy: PolicyResult

    risk: RiskResult

    approval: ApprovalResult

    employee: EmployeeResult