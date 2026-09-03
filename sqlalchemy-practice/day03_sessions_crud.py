import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase, Mapped, mapped_column
from models import Base, Patient, Appointment
load_dotenv(Path(__file__).with_name(".env"))

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME")

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}", echo=True)

# Task 1:
# - Insert a real new patient via session.add() + commit(), NOT hardcoding an id
# - Predict before running: after commit, will the Python object's .id attribute
#   automatically be filled in with the real database-assigned id, or will it stay None?

# It will be automatically filled in with the real database-assigned id. When you add a new object to the session and commit it, SQLAlchemy will automatically retrieve the generated primary key from the database and populate the object's .id attribute with that value. This is part of SQLAlchemy's ORM functionality, which keeps the Python object in sync with the database state after a commit.
with Session(engine) as session:
    patient = Patient(name="Sara Khan", age=30)
    session.add(patient)
    session.commit()

# Task 2:
# - Use session.get(Patient, <the id from Task 1>) to fetch that patient back
# - Print their name and age
# - Predict: does this issue a new SQL query, or does SQLAlchemy just hand you
#   back the same Python object from Task 1 without touching the database?

# It does not issue a new SQL query; SQLAlchemy just hands you back the same Python object from Task 1 without touching the database. When you use session.get() to retrieve an object that has already been added to the session and committed, SQLAlchemy will return the cached instance of that object from the session's identity map, rather than querying the database again. This behavior is part of SQLAlchemy's session management, which helps optimize performance by avoiding unnecessary database queries for objects that are already in memory.
with Session(engine) as session:
    patient = session.get(Patient, 1)
    all_patients = session.query(Patient).all()
    print(patient.name, patient.age)

# Task 3:
# - Fetch the patient again, change their age, commit
# - Reopen a session, fetch again, print the age
# - Predict whether the change persisted before running

# The change persisted. When you fetch the patient, modify their age, and commit the session, SQLAlchemy will generate an UPDATE statement to persist the changes to the database. After committing, if you reopen a new session and fetch the same patient again, you should see the updated age value, confirming that the change was successfully saved to the database.
with Session(engine) as session:
    patient = session.get(Patient, 1)
    patient.age = 36
    session.commit()

# Task 4:
# - Insert one Appointment linked only by patient_name (not a real foreign key yet —
#   that's Day 4), commit
# - Then delete it, commit, confirm with session.get() that it's actually gone (should return None)

# The appointment will be successfully deleted. When you add a new Appointment object to the session and commit it, it will be saved to the database. After that, when you delete the appointment and commit the session again, SQLAlchemy will generate a DELETE statement to remove the record from the database. When you use session.get() to fetch the appointment by its primary key after deletion, it should return None, indicating that the appointment no longer exists in the database.
with Session(engine) as session:
    appointment = Appointment(patient_name="Sara Khan", date="2026-09-10", reason="Checkup")
    session.add(appointment)
    session.commit()

with Session(engine) as session:
    appointment = session.get(Appointment, 1)

    if appointment is not None:
        session.delete(appointment)
        session.commit()
        print("Appointment 1 deleted")
    else:
        print("Appointment 1 was not found")
