# Task 1:
# Set up: import TestClient, import app from day07_serve_model, create client = TestClient(app)
# Write test_create_patient — POST with valid data, assert status_code == 201, assert response name matches what you sent

from fastapi.testclient import TestClient
from day07_serve_model import app
import pytest
client = TestClient(app)

def test_create_patient():
    response = client.post("/patients", json={"name": "Ali", "age": 25, "symptoms": ["fever"]})
    assert response.status_code == 201
    assert response.json()["name"] == "Ali"

# Task 2:
# Write test_get_nonexistent_patient_404 — GET a definitely-nonexistent id (e.g. 999999), assert status_code == 404

def test_get_nonexistent_patient_404():
    response = client.get("/patients/999999")
    assert response.status_code == 404

# Task 3:
# Write test_create_patient_invalid_age — POST with age as a string ("twenty") instead of int
# Before writing: predict which layer catches this — your own code, or Pydantic automatically? What status code results?

# Prediction: Pydantic will catch this automatically, before create_patient's body even runs,
# because "twenty" can't be coerced to int. Expect 422, not a custom error — this is the
# same automatic type validation as Day 1's /items/abc.
def test_create_patient_invalid_age():
    response = client.post("/patients", json={"name": "Ali", "age": "twenty", "symptoms": ["fever"]})
    assert response.status_code == 422

# Task 4:
# Write test_full_lifecycle — one test that chains create → get → delete → confirm-404, same sequence as Day 7's manual /docs test, now as code
# Use pytest.fixture for the sample patient data if you want to avoid repeating the same dict across tests (optional but good practice)

@pytest.fixture
def sample_patient():
    return {"name": "Ali", "age": 25, "symptoms": ["fever"]}

def test_full_lifecycle(sample_patient):
    create = client.post("/patients", json=sample_patient)
    assert create.status_code == 201
    patient_id = create.json()["id"]

    get_resp = client.get(f"/patients/{patient_id}")
    assert get_resp.status_code == 200
    assert get_resp.json()["name"] == "Ali"

    delete_resp = client.delete(f"/patients/{patient_id}")
    assert delete_resp.status_code == 204

    confirm = client.get(f"/patients/{patient_id}")
    assert confirm.status_code == 404

# Task 5:
# Run `pytest test_day07.py -v` from the fastapi-practice folder
# Paste the real terminal output — every test name with its pass/fail, not a summary claim