import os
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv(Path(__file__).with_name(".env"))

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST", "localhost")
db_port = os.getenv("DB_PORT", "5432")
db_name = os.getenv("DB_NAME")


# Task 1:
# - Install psycopg2-binary if not already present, confirm with pip show psycopg2-binary
# - Create an engine connected to your existing smartcare_clinic (or equivalent) Postgres database, echo=True
# - Predict: will engine = create_engine(...) alone actually open a network connection to Postgres? Write your prediction before running anything.

# Yes, I predict that engine = create_engine(...) alone will not open a network connection to Postgres. The create_engine function in SQLAlchemy is designed to set up the configuration for the database connection, but it does not establish the connection until an actual operation (like executing a query) is performed.
engine = create_engine(f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}", echo=True)

# Task 2:
# - Using engine.connect() and text(), SELECT all rows from a real table you already have (patients, or whatever exists from your SQL capstone)
# - Print each row
# - Predict how many rows will print, based on what you know is in that table, before running

# 2 rows will print, based on what I know is in that table.
conn = engine.connect()
result = conn.execute(text("SELECT * FROM patients"))
for row in result:
    print(row)

# Task 3:
# - Using text() and a bound parameter, INSERT one new test row into that table
# - Do NOT call conn.commit()
# - Close the connection, reopen a new one, SELECT again
# - Predict: will your inserted row be there or not? Write the prediction and the reasoning before running — this is the whole point of today's syntax note on commit()

# I predict that the inserted row will not be there when I reopen a new connection and SELECT again. This is because I did not call conn.commit() after the INSERT operation, which means that the changes made during that transaction will not be saved to the database. When the connection is closed, any uncommitted changes will be rolled back, and therefore the inserted row will not persist in the database.
conn.execute(text("INSERT INTO patients (name, age) VALUES (:name, :age)"), {"name": "Test Patient", "age": 30})
conn.close()

# Task 4:
# - Repeat the insert, this time calling conn.commit()
# - Reopen a new connection, SELECT again
# - Predict: will it be there now?
# - Clean up: DELETE your test row so you don't pollute the real table, and commit that too

# I predict that the inserted row will be there when I reopen a new connection and SELECT again. This is because I will call conn.commit() after the INSERT operation, which will save the changes made during that transaction to the database. When the connection is closed, the committed changes will persist in the database, and therefore the inserted row will be present when I query the table again.
conn = engine.connect()
conn.execute(text("INSERT INTO patients (name, age) VALUES (:name, :age)"), {"name": "Test Patient", "age": 30})
conn.commit()
conn.execute(text("DELETE FROM patients WHERE name = :name"), {"name": "Test Patient"})
conn.commit()