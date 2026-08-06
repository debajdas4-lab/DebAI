from pydantic import BaseModel

class ReceiptResult(BaseModel):

    vendor: str

    invoice_number: str

    expense_date: str

    currency: str

    amount: float

    taxes: float

    category: str

    confidence_score: float

    receipt_valid: bool