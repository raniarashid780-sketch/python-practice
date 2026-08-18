-- Task 1:
-- Create the full normalized SmartCare schema from scratch
-- doctors, patients, visits tables
-- All constraints: PRIMARY KEY, NOT NULL, UNIQUE, CHECK, REFERENCES
-- Drop tables first if they exist (correct order)

-- Drop old tables if they exist (correct order — children first)
DROP TABLE IF EXISTS visits;
DROP TABLE IF EXISTS patients;
DROP TABLE IF EXISTS doctors;

-- Create in correct order — parents first
CREATE TABLE doctors (
    id             SERIAL PRIMARY KEY,
    name           TEXT NOT NULL,
    specialization TEXT NOT NULL,
    phone          TEXT UNIQUE
);

CREATE TABLE patients (
    id   SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age  INTEGER CHECK(age > 0 AND age < 150)
);

CREATE TABLE visits (
    id         SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(id),
    doctor_id  INTEGER NOT NULL REFERENCES doctors(id),
    diagnosis  TEXT,
    visit_date DATE NOT NULL
);

-- Task 2:
-- Insert realistic data:
-- 3 doctors with different specializations
-- 5 patients
-- 8 visits (some patients visit multiple doctors)

-- Insert doctors
INSERT INTO doctors (name, specialization, phone) VALUES
    ('Dr. Sara', 'Cardiology',  '0300-1111111'),
    ('Dr. Ali',  'Neurology',   '0300-2222222'),
    ('Dr. Hina', 'Pediatrics',  '0300-3333333');

-- Insert patients
INSERT INTO patients (name, age) VALUES
    ('Ayesha', 25),
    ('Bilal',  32),
    ('Usman',  45),
    ('Fatima', 28);

-- Insert visits
INSERT INTO visits (patient_id, doctor_id, diagnosis, visit_date) VALUES
    (1, 1, 'Flu',      '2026-08-01'),
    (1, 2, 'Migraine', '2026-08-05'),
    (2, 1, 'Cold',     '2026-08-02'),
    (3, 3, 'Checkup',  '2026-08-03'),
    (4, 2, 'Anxiety',  '2026-08-04'),
    (1, 1, 'Checkup',  '2026-08-10');


-- Task 3:
-- Write a JOIN query that shows:
-- patient name, doctor name, diagnosis, visit_date
-- Order by visit_date ASC

SELECT p.name AS patient_name,
        d.name AS doctor_name,
        v.diagnosis,
        v.visit_date
FROM visits v
JOIN patients p ON v.patient_id = p.id
JOIN doctors d ON v.doctor_id = d.id
ORDER BY v.visit_date ASC;

-- Task 4:
-- Which doctor has the most visits?
-- Use GROUP BY + COUNT + ORDER BY
-- Show doctor name and visit_count

SELECT d.name,COUNT(*) AS visit_count
FROM visits v
JOIN doctors d ON v.doctor_id = d.id
GROUP BY d.name
ORDER BY visit_count DESC;

-- Task 5:
-- Which patients have visited MORE THAN ONE doctor?
-- Use GROUP BY + HAVING + COUNT(DISTINCT doctor_id)
-- Show patient name and how many different doctors they visited

SELECT p.name, COUNT(DISTINCT doctor_id) AS number_of_doctors_visited
FROM visits v
JOIN patients p ON v.patient_id = p.id
GROUP BY p.name
HAVING COUNT(DISTINCT doctor_id) > 1;