-- Task 1:
-- Create patients(id, name) and appointments(id, patient_id, date)
-- Insert 3 patients, 2 appointments (one patient must have zero appointments)

CREATE TABLE patients(
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE appointments(
    id SERIAL PRIMARY KEY,
    patient_id INTEGER,
    date DATE
);

INSERT INTO patients(name) VALUES
('Ayesha'),
('Bilal'),
('Hina');

INSERT INTO appointments (patient_id, date) VALUES
(1, '2026-08-15'),
(2, '2026-08-16');

-- Task 2:
-- Run INNER JOIN on patients and appointments
-- Show name, date
-- Count the rows returned — write the count as a comment above your query

-- It will 2 patients because nly 2 have appointments
SELECT p.name, a.date
FROM patients p
INNER JOIN appointments a ON p.id = a.patient_id;

-- Task 3:
-- Run LEFT JOIN on patients and appointments (patients on the left)
-- Show name, date
-- Count the rows returned — write the count as a comment above your query
-- Note which patient shows NULL

-- It will return all 3 patients but one which have no appointment will show null
SELECT p.name, a.date
FROM patients p
LEFT JOIN appointments a ON p.id = a.patient_id;

-- Task 4:
-- Swap the join direction: LEFT JOIN with appointments on the left, patients on the right
-- Show name, date
-- Explain in a comment why the row count is different (or isn't) from Task 3

--It will show just 2 rows because the left join is now on appointments, and there are only 2 appointments. The patient with no appointment will not be included in the result set.
SELECT p.name, a.date
FROM appointments a
LEFT JOIN patients p ON p.id = a.patient_id;

-- Task 5:
-- Using LEFT JOIN + WHERE, find the patient(s) with NO appointment at all
-- Show only their name
-- This must NOT be achievable with INNER JOIN — explain in a comment why not

-- INNER JOIN only returns rows where there is a match in both tables, so it cannot find patients with no appointments.
SELECT p.name
FROM patients p
LEFT JOIN appointments a ON p.id = a.patient_id
WHERE a.id IS NULL;