# Checkpoint: serve a real model (SmartCare-Clinic Patient, in-memory — no DB, no SQLAlchemy)

# TODO: predict-before-coding comment — what do you expect to differ from the Item toy project?

from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel, Field, field_validator

app = FastAPI()

# ---- Models ----
# PatientCreate: what a client sends (no id — the store assigns it)
# PatientOut: what you send back (id + everything else)
# TODO: pull the REAL fields from your SmartCare CLI/CSV code — don't guess

class PatientCreate(BaseModel):
    name : str = Field(..., min_length=1, max_length=50, description="Name of the patient, must be between 1 and 50 characters")
    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError("name cannot be blank or whitespace-only")
        return v
    age : int = Field(..., ge=0, description="Age of the patient, must be greater than or equal to 0")
    symptoms : list[str] = Field(..., description="List of symptoms the patient is experiencing")

class PatientOut(BaseModel):
    id: int
    name : str = Field(..., min_length=1, max_length=50, description="Name of the patient, must be between 1 and 50 characters")
    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, v):
        if not v.strip():
            raise ValueError("name cannot be blank or whitespace-only")
        return v
    age : int = Field(..., ge=0, description="Age of the patient, must be greater than or equal to 0")
    symptoms : list[str] = Field(..., description="List of symptoms the patient is experiencing")

# ---- Store ----
patients_db: dict[int, PatientOut] = {}
next_id = 1

# ---- Dependency ----
# Same shape as Day 6's get_item_or_404 — reuse the pattern, don't reinvent it
def get_patient_or_404(patient_id: int) -> PatientOut:
    if patient_id not in patients_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return patients_db[patient_id]

# ---- Endpoints ----
@app.post("/patients", status_code=201)
def create_patient(patient: PatientCreate):
    global next_id
    new_patient = PatientOut(id=next_id, **patient.model_dump())
    patients_db[next_id] = new_patient
    next_id += 1
    return new_patient

@app.get("/patients")
def list_patients():
    return list(patients_db.values())


@app.get("/patients/{patient_id}")
def get_patient(patient: PatientOut = Depends(get_patient_or_404)):
    return patient

@app.put("/patients/{patient_id}")
def update_patient(patient_id: int, updated: PatientCreate, existing: PatientOut = Depends(get_patient_or_404)):
    updated_patient = PatientOut(id=patient_id, **updated.model_dump())
    patients_db[patient_id] = updated_patient
    return updated_patient

@app.delete("/patients/{patient_id}", status_code=204)
def delete_patient(patient_id: int, existing: PatientOut = Depends(get_patient_or_404)):
    del patients_db[patient_id]
    return

# Task 5 — Full CRUD verification via /docs
# Fill in each blank with REAL output you actually saw. No predictions, no descriptions.

# 5a. POST /patients — create Patient A
# Status: 201   Body: {"id": 1,"name": "Maaz","age": 20,"symptoms": ["flu", "fever"]}

# 5b. POST /patients — create Patient B
# Status: 201  Body: {"id": 2,"name": "Ali","age": 25,"symptoms": ["heart pain","chest pain"]}

# 5c. GET /patients — list all
# Status: 200  Body: {"id": 1,"name": "Maaz","age": 20,"symptoms": ["flu", "fever"]}, {"id": 2,"name": "Ali","age": 25,"symptoms": ["heart pain","chest pain"]}

# 5d. GET /patients/{id} — valid id (Patient A's id)
# Status: 200   Body: {"id": 1,"name": "Maaz","age": 20,"symptoms": ["flu", "fever"]}

# 5e. GET /patients/{id} — invalid id (one that doesn't exist)
# Status: 404  Body: {"detail": "Item not found"}

# 5f. PUT /patients/{id} — valid id, change age and/or symptoms
# Status: 200   Body: {"id": 1,"name": "Maaz","age": 25,"symptoms": ["flu","fever","Cough","Nausea"]}

# 5g. PUT /patients/{id} — invalid id
# Status: 404    Body: {"detail": "Item not found"}

# 5h. DELETE /patients/{id} — valid id (use Patient B's id)
# Status: 204   Body: (body is empty)

# 5i. GET /patients/{id} — same id you just deleted in 5h
# Status: 404   Body: {"detail": "Item not found"}

# Task 6 — Validator edge cases (test name and age constraints)
# Fill in each blank with REAL output you actually saw. No predictions, no descriptions.

# 6a. POST /patients — create with blank name (only whitespace)
# Status: 422   Body: {"detail":[{"type":"value_error","loc":["body","name"],"msg":"Value error, name cannot be blank or whitespace-only","input":"   ","ctx":{}}]}

# 6b. POST /patients — create with name exceeding 50 characters
# Status: 422   Body: {"detail":[{"type":"string_too_long","loc":["body","name"],"msg":"String should have at most 50 characters","input":"this is a very long name that exceeds the maximum of fifty characters allowed","ctx":{"max_length":50}}]}

# 6c. POST /patients — create with negative age
# Status: 422   Body: {"detail":[{"type":"greater_than_equal","loc":["body","age"],"msg":"Input should be greater than or equal to 0","input":-5,"ctx":{"ge":0}}]}

# 6d. POST /patients — create with valid data and empty symptoms list
# Status: 201   Body: {"id":3,"name":"Valid Patient","age":30,"symptoms":[]}

# Task 7 — Multiple patient workflow with updates
# Fill in each blank with REAL output you actually saw. No predictions, no descriptions.

# 7a. POST /patients — create Patient X
# Status: 201   Body: {"id":4,"name":"Patient X","age":35,"symptoms":["headache","fatigue"]}

# 7b. POST /patients — create Patient Y
# Status: 201   Body: {"id":5,"name":"Patient Y","age":42,"symptoms":["back pain","insomnia"]}

# 7c. PUT /patients/{id} — update Patient X's symptoms only (add one new symptom)
# Status: 200   Body: {"id":4,"name":"Patient X","age":35,"symptoms":["headache","fatigue","dizziness"]}

# 7d. GET /patients — verify both patients exist with correct data
# Status: 200   Body: [{"id":4,"name":"Patient X","age":35,"symptoms":["headache","fatigue","dizziness"]},{"id":5,"name":"Patient Y","age":42,"symptoms":["back pain","insomnia"]}]

# 7e. DELETE /patients/{id} — delete Patient X
# Status: 204   Body: (body is empty)

# 7f. GET /patients — verify only Patient Y remains
# Status: 200   Body: [{"id":5,"name":"Patient Y","age":42,"symptoms":["back pain","insomnia"]}]
