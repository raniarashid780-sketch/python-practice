-- Task 1:
-- Simulate a RIGHT JOIN using LEFT JOIN table swap
-- Use appointments and patients tables
-- Show patient name and appointment date
-- All appointments must appear, even if patient is missing

SELECT p.name, a.date
FROM appointments a
LEFT JOIN patients p ON a.patient_id = p.id;

-- Task 2:
-- Run a FULL OUTER JOIN on patients and appointments
-- Show name and date
-- How many rows come back? Write the count as a comment

SELECT p.name, a.date
FROM patients p
FULL OUTER JOIN appointments a ON p.id = a.patient_id;
-- Count: 3 rows

-- Task 3:
-- Self-join on employees table
-- Show each employee's name and their manager's name
-- CEO (Sara) should show NULL for manager
-- Use LEFT JOIN so Sara is included

SELECT e.name AS employee_name, m.name AS manager_name
FROM employees e
LEFT JOIN employees m ON e.manager_id = m.id;

-- Task 4:
-- Self-join: find all employees who report directly to Sara
-- Show only their names
-- Do NOT hardcode Sara's id — use a subquery or join condition

SELECT e.name
FROM employees e
JOIN employees m ON e.manager_id = m.id
WHERE m.name = 'Sara';

-- Task 5:
-- Using your patients + appointments tables
-- Find patients who HAVE appointments (INNER JOIN)
-- AND in the same query show patients who DO NOT (anti-join)
-- Combine both results using UNION
-- Add a column called status that says 'has appointment' or 'no appointment'

SELECT p.name, 'has appointment' AS status
FROM patients p
INNER JOIN appointments a ON p.id = a.patient_id
UNION
SELECT p.name, 'no appointment' AS status
FROM patients p
LEFT JOIN appointments a ON p.id = a.patient_id
WHERE a.patient_id IS NULL;