-- Task 1:
-- Create a doctors table with ALL these constraints:
--   id: SERIAL PRIMARY KEY
--   name: TEXT NOT NULL
--   specialization: TEXT NOT NULL
--   phone: TEXT UNIQUE
--   experience_yrs: INTEGER, must be >= 0 (CHECK constraint)
--   created_at: TIMESTAMP DEFAULT NOW()

CREATE TABLE doctors (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    specialization TEXT NOT NULL,
    phone TEXT UNIQUE,
    experience_yrs INTEGER CHECK (experience_yrs >= 0),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Task 2:
-- Create a patients table with:
--   id: SERIAL PRIMARY KEY
--   name: TEXT NOT NULL
--   age: INTEGER CHECK age between 1 and 150
--   doctor_id: INTEGER REFERENCES doctors(id)
-- Then insert 2 doctors and 4 patients (2 per doctor)

CREATE TABLE patients (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER CHECK(age > 0 AND age < 150),
    doctor_id INTEGER REFERENCES doctors(id)
);
INSERT INTO doctors (name, specialization, phone, experience_yrs)
VALUES
    ('Dr Sara', 'Cardiology', '0300-1111111', 10),
    ('Dr. Ali',   'Neurology',   '0300-2222222',  8);

-- Task 3:
-- UPDATE Dr. Sara's experience_yrs to 15
-- UPDATE all patients of doctor_id=1 — change their doctor to doctor_id=2
-- Show the patients table after both updates

UPDATE doctors
SET experience_yrs = 15
WHERE name = 'Dr Sara';
UPDATE patients
SET doctor_id = 2
WHERE doctor_id = 1;


-- Task 4:
-- Try to INSERT a patient with doctor_id = 999 (does not exist)
-- Write what error PostgreSQL gives as a comment
-- Then INSERT a valid patient correctly

INSERT INTO patients (name, age, doctor_id)
VALUES
    ('Patient X', 30, 999);
-- ERROR: insert or update on table "patients" violates foreign key constraint "patients_doctor_id_fkey"
INSERT INTO patients (name, age, doctor_id)
VALUES
    ('Wania', 20, 2);
SELECT * FROM patients;

-- Task 5:
-- Use a transaction:
--   BEGIN
--   DELETE all patients WHERE age < 25
--   SELECT COUNT(*) to see how many remain
--   ROLLBACK — undo the delete
--   SELECT COUNT(*) again to confirm rows came back
-- Write what you observe as a comment

BEGIN;
DELETE  FROM patients WHERE age < 25;
SELECT COUNT(*) AS no_of_patients
FROM patients;
ROLLBACK;
SELECT COUNT(*) AS no_of_patients
FROM patients;
--I observed that the count remains the same as before the transaction
