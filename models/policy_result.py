from pydantic import BaseModel

class PolicyResult(BaseModel):

    compliant: bool

    violated_rules: list[str]

    reimbursement_limit: float

    comments: str