import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

load_dotenv(Path(__file__).with_name(".env"))

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME")

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}", echo=True)
conn = engine.connect()

# Task 0:
# - Confirm your existing `patients` table columns match what you're about to declare
#   (you already have id, name, age — don't guess again like last time)

# Confirmed: the existing `patients` table has the following columns:
# - id (integer, primary key)
# - name (string)
# - age (integer)

# Task 1:
# - Define Base(DeclarativeBase) and a Patient class mapping to the real "patients" table
# - Match its columns exactly to what's really in Postgres
# - Predict: if you call Base.metadata.create_all(engine) right now, will it create
#   a NEW patients table, error out, or silently do nothing since the table already exists?
#   Write your prediction with reasoning before running.

# Calling Base.metadata.create_all(engine) right now will silently do nothing since the table already exists. The create_all() method checks for the existence of the tables defined in the metadata and will only create them if they do not already exist. Since the "patients" table is already present in the database, it should not attempt to recreate it or throw an error.
class Base(DeclarativeBase):
    pass

class Patient(Base):
    __tablename__ = "patients"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    age: Mapped[int]

# Task 2:
# - Call Base.metadata.create_all(engine) and observe what actually happens (echo=True will show you)
# - Confirm your prediction was right or wrong — don't just move on if you were wrong, explain why

Base.metadata.create_all(engine)
# Task 2 observation: When I called Base.metadata.create_all(engine), it did not create a new "patients" table, and there were no errors. This confirms my prediction that the method would silently do nothing since the table already exists. The create_all() method checks for the existence of the tables defined in the metadata and only creates them if they do not already exist, which is why it did not attempt to recreate the "patients" table.

# Task 3:
# - Create a second, brand-new table via a class: Appointment
#   - id (primary key), patient_name (str), date (str is fine for now, real Date type comes later), reason (str)
# - Predict: will create_all() create ONLY the new Appointment table, or try to recreate Patient too?
# - Run it and verify against your prediction

# It will create_all() create ONLY the new Appointment table, and it will not attempt to recreate the Patient table. The create_all() method checks for the existence of each table defined in the metadata and only creates those that do not already exist. Since the "patients" table already exists, it should only create the new "appointments" table.
class Appointment(Base):
    __tablename__ = "Appointments"

    id: Mapped[int] = mapped_column(primary_key=True)
    patient_name: Mapped[str]
    date: Mapped[str]
    reason: Mapped[str]

Base.metadata.create_all(engine)

# Task 3 observation: When I called Base.metadata.create_all(engine) after defining the Appointment class, it created only the new "appointments" table and did not attempt to recreate the "patients" table. This confirms my prediction that create_all() would only create the new table since the "patients" table already exists in the database. The method checks for the existence of each table defined in the metadata and only creates those that do not already exist.

# Task 4:
# - Instantiate a Patient object in Python (don't insert it into the DB yet — that's Day 3, sessions)
# - Print the object directly: print(patient_instance)
# - Predict what this print will show BEFORE running — a memory address, or the field values?
#   (Hint: this is testing whether you understand that __repr__ isn't automatic — you haven't written one)

# print will show the memory address of the Patient object, not the field values. This is because the default __repr__ method inherited from the base object class does not provide a human-readable representation of the object's attributes. Since we haven't defined a custom __repr__ method for the Patient class, it will display the default representation, which includes the class name and memory address.
print("\nTask 4:")
print(patient_instance := Patient(id=1, name="John Doe", age=30))