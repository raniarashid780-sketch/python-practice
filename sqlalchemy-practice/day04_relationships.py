import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import  Session
from models import Patient, Appointment

load_dotenv(Path(__file__).with_name(".env"))

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME")

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}", echo=True)


# Task 0:
# - Update models.py exactly as above. This changes appointments' schema —
#   your practice DB's old appointments table (with patient_name) won't match.
#   Predict: will Base.metadata.create_all(engine) fix this automatically, or do
#   you need to drop the old table first? (Hint: reread what create_all does — Day 2.)

# Base.metadata.create_all(engine) will not fix the schema of the existing appointments table automatically. The create_all() method only creates tables that do not already exist in the database; it does not modify existing tables or their schemas. Therefore, if the appointments table already exists with a different schema (e.g., using patient_name instead of patient_id), you will need to drop the old table first before calling create_all() to create the new table with the updated schema.

# Task 1:
# - Drop and recreate as needed based on your Task 0 answer, confirm the new schema
# - Insert one real Patient, commit, note their id

with Session(engine) as session:
    patient = Patient(name="Ali Khan", age=39)
    session.add(patient)
    print(f"Inserted patient with id: {patient.id}")  # This will print the id after commit
    session.commit()

# Task 2:
# - Insert 2 Appointments linked to that patient via patient_id (not patient_name)
# - Predict: what happens if you try inserting an Appointment with patient_id=999,
#   a patient that doesn't exist? Write the prediction, then actually try it.

# It will raise an IntegrityError due to a foreign key constraint violation. Since the appointments table has a foreign key relationship with the patients table, trying to insert an Appointment with a patient_id that does not exist in the patients table (like 999) will violate the foreign key constraint, and the database will reject the insertion, resulting in an error.
with Session(engine) as session:
    appt1 = Appointment(patient_id=1, date="2026-09-10", reason="Checkup")
    appt2 = Appointment(patient_id=1, date="2026-09-15", reason="Follow-up")
    session.add_all([appt1, appt2])
    session.commit()

# with Session(engine) as session:
#     appt3 = Appointment(patient_id=9999, date="2026-09-15", reason="Follow-up")
#     session.add(appt3)
#     session.commit()
# Whem I try to enter the appointment whose patient_id does not exist i got this error
# sqlalchemy.exc.IntegrityError: (psycopg2.errors.ForeignKeyViolation) insert or update on table "appointments" violates foreign key constraint "appointments_patient_id_fkey"
# DETAIL:  Key (patient_id)=(9999) is not present in table "patients".


# Task 3:
# - Fetch the Patient with session.get(), then print patient.appointments
# - Predict what this prints before running — a list of Appointment objects,
#   raw ids, or something else?

# It will print a list of Appointment objects. When you access the patient.appointments relationship, SQLAlchemy will return a list of Appointment instances that are associated with that Patient through the foreign key relationship. Each item in the list will be an instance of the Appointment class, allowing you to access their attributes and methods.
with Session(engine) as session:
    patient = session.get(Patient, 1)
    all_patients = session.query(Patient).all()
    print(patient.appointments)  # This will print a list of Appointment objects associated with the patient.

# Task 4:
# - Fetch one Appointment, print appointment.patient.name
# - This is the "many-to-one" direction working — confirm it gives you the right name


with Session(engine) as session:
    appointment = session.get(Appointment, 1)
    all_appointments = session.query(Appointment).all()
    print(appointment.patient.name)