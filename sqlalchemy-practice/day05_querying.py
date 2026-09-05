import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, select, func
from sqlalchemy.orm import Session
from models import Patient, Appointment

load_dotenv(Path(__file__).with_name(".env"))

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME")

engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}", echo=True)
session = Session(engine)

# Task 1:
# - select() all patients over age 30, print names
# - Predict: .scalars().all() vs plain .all() here — which do you need, and why?

# .scalars().all() is needed here because we are selecting a single column (Patient) and want to retrieve the results as a list of Patient objects. Using plain .all() would return a list of Row objects, which would require additional unpacking to access the Patient instances. By using .scalars(), we directly get the Patient instances without the need for further processing.
stmt = select(Patient).where(Patient.age > 30)
patients = session.execute(stmt).scalars().all()
print([patient.name for patient in patients])  # This will print the names of patients over age 30.

# Task 2:
# - Join Patient + Appointment, select patient name + appointment reason
# - Predict how many rows you get if one patient has 2 appointments and
#   another has 0 (this is what a JOIN actually does to row count — check your SQL notes)

# You will get 2 rows in the result set. The JOIN operation combines rows from both tables based on the specified condition (in this case, the relationship between Patient and Appointment). Since one patient has 2 appointments, there will be 2 rows for that patient, each corresponding to one of their appointments. The patient with 0 appointments will not contribute any rows to the result set, as there are no matching records in the Appointment table for that patient. Therefore, the total number of rows returned will be equal to the number of appointments for patients who have at least one appointment.
stmt = select(Patient.name, Appointment.reason).join(Appointment)
appointments = session.execute(stmt).all()
print(appointments)  # This will print the list of tuples containing patient names and their corresponding appointment reasons.

# Task 3:
# - Count appointments per patient using func.count() + group_by()
# - Predict: does the patient with 0 appointments appear in this result at all?
#   (Hint: plain join() vs join with different semantics — this is worth getting wrong once)

# The patient with 0 appointments will not appear in the result of this query. When using a plain join() in SQLAlchemy (which translates to an INNER JOIN in SQL), only patients who have at least one matching appointment will be included in the result set. Patients with no appointments will be excluded because there are no corresponding rows in the Appointment table to join with. If you want to include patients with 0 appointments, you would need to use an outer join (LEFT JOIN) instead of a plain join.
stmt = select(Patient.name, func.count(Appointment.id)).join(Appointment).group_by(Patient.id)
appointment_counts = session.execute(stmt).all()
print(appointment_counts)

# Task 4:
# - Filter with .where() combined with the join from Task 2 — get only appointments
#   with reason "Checkup", print the patient names attached to them

# You will get a list of patient names who have appointments with the reason "Checkup". The .where() clause filters the results of the join to only include rows where the Appointment.reason is equal to "Checkup". This means that only patients who have at least one appointment with that specific reason will be included in the final result set. If a patient has no appointments or only appointments with different reasons, they will not appear in the output.
stmt = select(Patient.name).join(Appointment).where(Appointment.reason == "Checkup")
checkup_patients = session.execute(stmt).scalars().all()
print(checkup_patients)