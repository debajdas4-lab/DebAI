from pydantic import BaseModel

class ExpenseRequest(BaseModel):

    employee_name: str
    employee_id: str
    department: str

    expense_type: str

    amount: float

    comments: str

    receipt_file: str

    receipt_name: str