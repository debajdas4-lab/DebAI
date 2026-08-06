from pydantic import BaseModel

class ApprovalResult(BaseModel):

    decision: str

    confidence: float

    approver: str

    justification: str