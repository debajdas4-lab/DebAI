from pydantic import BaseModel

class EmployeeResult(BaseModel):

    message: str

    next_steps: list[str]