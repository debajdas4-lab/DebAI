from pydantic import BaseModel

class RiskResult(BaseModel):

    risk_score: float

    duplicate_receipt: bool

    fraud_probability: float

    observations: list[str]