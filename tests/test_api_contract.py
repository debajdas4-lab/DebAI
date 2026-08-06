import base64
import os
import sys
from pathlib import Path

from fastapi.testclient import TestClient

sys.path.insert(0, str(Path(__file__).parents[1]))
os.environ.setdefault("API_KEY", "test-key")

from api.main import app  # noqa: E402


def test_health_check():
    response = TestClient(app).get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "Running"


def test_json_contract_rejects_invalid_base64():
    payload = {
        "employee_name": "Test User",
        "employee_id": "E-1",
        "department": "IT",
        "expense_type": "Meals",
        "amount": 100,
        "receipt_name": "receipt.pdf",
        "receipt_base64": "not-base64",
    }
    response = TestClient(app).post("/v1/expenses", json=payload, headers={"x-api-key": "test-key"})
    assert response.status_code == 422
