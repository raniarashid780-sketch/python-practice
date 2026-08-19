-- ============================================
-- SmartCare-Clinic PostgreSQL Backend
-- SQL Track Capstone — Day 14
-- ============================================

-- SECTION 1: SCHEMA SETUP
-- Drop in child-first order
-- Create in parent-first order
-- All tables must have:
--   SERIAL PRIMARY KEY
--   NOT NULL where appropriate
--   CHECK constraints where appropriate
--   FOREIGN KEY references
--   DEFAULT NOW() on timestamp columns

DROP TABLE IF EXISTS visits;
DROP TABLE IF EXISTS patients;
DROP TABLE IF EXISTS doctors;

-- Tables to create:
-- doctors(id, name, specialization, phone, experience_yrs, created_at)
-- patients(id, name, age, phone, created_at)
-- visits(id, patient_id, doctor_id, diagnosis, visit_date, fee)

CREATE TABLE doctors (
    id             SERIAL PRIMARY KEY,
    name           TEXT NOT NULL,
    specialization TEXT NOT NULL,
    phone          TEXT UNIQUE,
    experience_yrs INTEGER CHECK (experience_yrs >= 0),
    created_at     TIMESTAMP DEFAULT NOW()
);

CREATE TABLE patients (
    id   SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    age  INTEGER CHECK(age > 0 AND age < 150),
    phone TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE visits (
    id         SERIAL PRIMARY KEY,
    patient_id INTEGER NOT NULL REFERENCES patients(id),
    doctor_id  INTEGER NOT NULL REFERENCES doctors(id),
    diagnosis  TEXT,
    visit_date DATE NOT NULL,
    fee        DECIMAL(10, 2) CHECK(fee >= 0)
);

-- SECTION 2: DATA
-- Insert minimum:
-- 4 doctors (different specializations)
-- 6 patients
-- 10 visits (patients must visit multiple doctors to make queries interesting)

INSERT INTO doctors (name, specialization, phone, experience_yrs)
    VALUES
    ('Dr. Sara', 'Cardiology', '0300-1111111', 11),
    ('Dr. Ali', 'Neurology', '0300-2222222', 9),
    ('Dr. Hina', 'Pediatrics', '0300-3333333', 7),
    ('Dr. Omar', 'Dermatology', '0300-4444444', 5);

INSERT INTO patients(name, age, phone)
    VALUES
    ('Wania', 32, '0333-1111111'),
    ('Ayesha', 25, '0333-2222222'),
    ('Bilal', 40, '0333-3333333'),
    ('Usman', 50, '0333-4444444'),
    ('Fatima', 28, '0333-5555555'),
    ('Zain', 35, '0333-6666666');

INSERT INTO visits(patient_id, doctor_id, diagnosis, visit_date, fee)
    VALUES
    (1, 1, 'Flu', '2026-08-01', 100.00),
    (1, 2, 'Migraine', '2026-08-05', 150.00),
    (2, 1, 'Cold', '2026-08-02', 80.00),
    (3, 3, 'Checkup', '2026-08-03', 120.00),
    (4, 2, 'Anxiety', '2026-08-04', 200.00),
    (5, 4, 'Skin Rash', '2026-08-06', 90.00),
    (6, 1, 'Heart Checkup', '2026-08-07', 250.00),
    (2, 3, 'Vaccination', '2026-08-08', 60.00),
    (3, 4, 'Acne Treatment', '2026-08-09', 110.00),
    (5, 2, 'Stress Management', '2026-08-10', 180.00);

-- SECTION 3: ANALYTICAL QUERIES
-- Write all 5 queries below

-- Query 1 — JOIN query:
-- Show full visit report:
-- patient name, doctor name, specialization,
-- diagnosis, visit_date, fee
-- Order by visit_date DESC

SELECT p.name AS patient_name,
       d.name AS doctor_name,
       d.specialization,
       v.diagnosis,
       v.visit_date,
       v.fee
FROM visits v
JOIN patients p ON v.patient_id = p.id
JOIN doctors d ON v.doctor_id = d.id
ORDER BY v.visit_date DESC;

-- Query 2 — GROUP BY + HAVING:
-- Which doctors have seen more than 2 patients?
-- Show doctor name, specialization, patient_count
-- Order by patient_count DESC

SELECT d.name AS doctor_name,
       d.specialization,
       COUNT(DISTINCT v.patient_id) AS patient_count
FROM visits v
JOIN doctors d ON v.doctor_id = d.id
GROUP BY d.name, d.specialization
HAVING COUNT(DISTINCT v.patient_id) > 2
ORDER BY patient_count DESC;

-- Query 3 — Subquery or CTE:
-- Find all visits where the fee is above
-- the average fee across all visits
-- Show patient name, doctor name, fee, visit_date
-- Order by fee DESC

WITH average_fee AS (
    SELECT AVG(fee) AS avg_fee
    FROM visits
)
SELECT p.name AS patient_name,
       d.name AS doctor_name,
       v.fee,
       v.visit_date
FROM average_fee
JOIN visits v ON v.fee > avg_fee
JOIN patients p ON v.patient_id = p.id
JOIN doctors d ON v.doctor_id = d.id
ORDER BY fee DESC;

-- Query 4 — Window function:
-- Rank doctors by total revenue (SUM of fees)
-- Use RANK() OVER(ORDER BY total_revenue DESC)
-- Show doctor name, total_revenue, revenue_rank
-- Use a CTE to calculate totals first

WITH doctor_revenue AS (
    SELECT d.name AS doctor_name,
           SUM(v.fee) AS total_revenue
    FROM visits v
    JOIN doctors d ON v.doctor_id = d.id
    GROUP BY d.name
)
SELECT doctor_name,
       total_revenue,
       RANK() OVER(ORDER BY total_revenue DESC) AS revenue_rank
FROM doctor_revenue;

-- Query 5 — Advanced:
-- For each doctor show:
--   doctor name
--   total_visits
--   total_revenue
--   avg_fee (rounded to 2 decimal places)
--   most_common_diagnosis (the diagnosis that appears most for that doctor)
-- The most_common_diagnosis is the hardest part —
-- use a subquery or think about how to find the mode per group

WITH doctor_stats AS (
    SELECT d.name AS doctor_name,
           COUNT(v.id) AS total_visits,
           SUM(v.fee) AS total_revenue,
           ROUND(AVG(v.fee), 2) AS avg_fee
    FROM visits v
    JOIN doctors d ON v.doctor_id = d.id
    GROUP BY d.name
),
most_common_diagnosis AS (
    SELECT d.id AS doctor_id,
           d.name AS doctor_name,
           v.diagnosis AS most_common_diagnosis
    FROM visits v
    JOIN doctors d ON v.doctor_id = d.id
    GROUP BY d.id, d.name, v.diagnosis
    HAVING COUNT(*) = (
        SELECT MAX(diagnosis_count)
        FROM (
            SELECT COUNT(*) AS diagnosis_count
            FROM visits v2
            WHERE v2.doctor_id = d.id
            GROUP BY v2.diagnosis
        ) AS counts
    )
)
SELECT ds.doctor_name,
       ds.total_visits,
       ds.total_revenue,
       ds.avg_fee,
       mcd.most_common_diagnosis
FROM doctor_stats ds
LEFT JOIN most_common_diagnosis mcd ON ds.doctor_name = mcd.doctor_name
ORDER BY ds.total_revenue DESC;