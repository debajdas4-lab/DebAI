"""
Expense AI Assistant API

Author : D. J. Das
Version: 1.0.0
"""

from pathlib import Path
import uuid
import base64
import binascii
from typing import Any

from fastapi import (
    FastAPI,
    UploadFile,
    File,
    Form,
    Header,
    HTTPException,
)

from config import Config
from flows.expense_flow import ExpenseFlow
from pydantic import BaseModel, Field

# ---------------------------------------------------------
# FastAPI Application
# ---------------------------------------------------------

app = FastAPI(
    title=Config.APP_NAME,
    version=Config.APP_VERSION,
    description="Enterprise Expense AI Assistant"
)


class ExpenseJsonRequest(BaseModel):
    """Power Automate-friendly JSON contract."""

    employee_name: str = Field(min_length=1)
    employee_id: str = Field(min_length=1)
    department: str = Field(min_length=1)
    expense_type: str = Field(min_length=1)
    amount: float = Field(gt=0)
    comments: str = ""
    receipt_name: str = Field(min_length=1)
    receipt_base64: str = Field(min_length=1)


def _run_expense(expense_data: dict[str, Any]) -> dict[str, Any]:
    result = ExpenseFlow().kickoff(inputs=expense_data)
    return {"status": "Success", "data": getattr(result, "raw", str(result))}


# ---------------------------------------------------------
# Create Upload Folder
# ---------------------------------------------------------

Path(Config.UPLOAD_FOLDER).mkdir(
    parents=True,
    exist_ok=True
)


# ---------------------------------------------------------
# Health Check
# ---------------------------------------------------------

@app.get("/")
async def root():

    return {
        "status": "Running",
        "application": Config.APP_NAME,
        "version": Config.APP_VERSION
    }


# ---------------------------------------------------------
# Expense Submission Endpoint
# ---------------------------------------------------------

@app.post("/submit-expense")
async def submit_expense(

    employee_name: str = Form(...),

    employee_id: str = Form(...),

    department: str = Form(...),

    expense_type: str = Form(...),

    amount: float = Form(...),

    comments: str = Form(...),

    receipt: UploadFile = File(...),

    x_api_key: str = Header(...)
):

    # -----------------------------------------------------
    # Authenticate
    # -----------------------------------------------------

    if x_api_key != Config.API_KEY:

        raise HTTPException(
            status_code=401,
            detail="Invalid API Key"
        )

    # -----------------------------------------------------
    # Save Uploaded Receipt
    # -----------------------------------------------------

    unique_filename = (
        f"{uuid.uuid4()}_{receipt.filename}"
    )

    file_path = (
        Path(Config.UPLOAD_FOLDER) /
        unique_filename
    )

    file_bytes = await receipt.read()

    with open(file_path, "wb") as f:
        f.write(file_bytes)

    # -----------------------------------------------------
    # Build Expense Data
    # -----------------------------------------------------

    expense_data = {

        "employee_name": employee_name,

        "employee_id": employee_id,

        "department": department,

        "expense_type": expense_type,

        "amount": amount,

        "comments": comments,

        "receipt_file": str(file_path),

        "receipt_name": receipt.filename

    }

    # -----------------------------------------------------
    # Start CrewAI Flow
    # -----------------------------------------------------

    flow = ExpenseFlow()

    result = flow.kickoff(inputs=expense_data)

    # -----------------------------------------------------
    # Return Response
    # -----------------------------------------------------

    return {

        "status": "Success",

        "message":
        "Expense processed successfully.",

        "data": getattr(result, "raw", str(result))

    }


@app.post("/v1/expenses")
async def submit_expense_json(
    request: ExpenseJsonRequest,
    x_api_key: str = Header(...),
):
    """JSON endpoint for a Power Automate HTTP trigger."""
    if x_api_key != Config.API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    try:
        file_bytes = base64.b64decode(request.receipt_base64, validate=True)
    except (binascii.Error, ValueError) as exc:
        raise HTTPException(status_code=422, detail="receipt_base64 is invalid") from exc

    safe_name = Path(request.receipt_name).name
    file_path = Path(Config.UPLOAD_FOLDER) / f"{uuid.uuid4()}_{safe_name}"
    file_path.write_bytes(file_bytes)
    payload = request.model_dump(exclude={"receipt_base64"})
    payload["receipt_file"] = str(file_path)
    return _run_expense(payload)
