-- Day 1: What is a database? + PostgreSQL Setup
-- ================================================

-- Q1: Without IF NOT EXISTS, PostgreSQL throws:
--     ERROR: relation "students" already exists
--     IF NOT EXISTS makes the statement idempotent —
--     safe to run multiple times without crashing.

-- Q2: We skip 'id' in INSERT because SERIAL automatically
--     calls nextval() on the sequence. Providing id manually
--     risks conflicting with the sequence counter later.

-- Create database (run once in psql or DBeaver)
-- CREATE DATABASE practice;

-- Create table
CREATE TABLE IF NOT EXISTS students (
    id    SERIAL PRIMARY KEY,
    name  TEXT   NOT NULL,
    age   INTEGER
);

-- Insert rows
INSERT INTO students (name, age) VALUES ('Rania', 20);
INSERT INTO students (name, age) VALUES ('Sara', 22);
INSERT INTO students (name, age) VALUES ('Ali', 19);

-- View all data
SELECT * FROM students;

-- Inspect table structure (SQL standard way)
SELECT column_name, data_type, is_nullable
FROM information_schema.columns
WHERE table_name = 'students';