# SmartCare-Clinic Patient API (Capstone)

A small web API for managing patients in a clinic — the same Patient
model (name, age, symptoms) as the SmartCare-Clinic project, exposed
as a web service instead of a terminal program.

## What it does
- Create a patient record
- List all patients
- Look up a patient by id
- Update a patient's record
- Delete a patient

## Built with
- FastAPI
- Docker
- pytest (testing)

## Running it
    docker compose up --build

Then visit http://127.0.0.1:8000/docs to use the API interactively.

## Testing it
    python -m pytest test_day07.py -v