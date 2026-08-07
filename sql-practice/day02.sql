-- Day 2: SELECT, FROM, WHERE
-- ===========================

-- Q: In what order does PostgreSQL execute SELECT, FROM, WHERE?
-- A: From   Go to table mentioned
--    Where  keep the rows where condition is true and throw away all where condition is false
--    Select From what is left show me only column names

-- Task 1: All columns and all rows from jobs

SELECT * FROM jobs;

-- Task 2: Only title and budget columns
SELECT  title, budget FROM jobs;

-- Task 3: Jobs where budget > 500
SELECT * FROM jobs WHERE budget > 500;

-- Task 4: Jobs where category = 'Automation
-- Remember: case sensitive
SELECT * FROM jobs WHERE category = 'Automation';

-- Task 5: Return title and a new column called daily_rate
-- which is budget divided by 30
SELECT title, budget, budget/ 30 AS daily_rate
FROM jobs: