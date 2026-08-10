-- Task 1:
-- How many total rows are in your jobs table?
-- How many rows have a non-NULL budget?
-- Show both in one query with aliases total_jobs and jobs_with_budget
SELECT COUNt(*) AS total_jobs,
    COUNT(budget) AS jobs_with_budget
FROM jobs;

-- Task 2:
-- What is the average budget across ALL jobs?
-- Round to 2 decimal places
-- Alias it avg_budget
SELECT ROUND(AVG(REPLACE(budget, '$', '')::NUMERIC), 2) AS avg_budget
FROM job;
-- Task 3:
-- What is the minimum and maximum budget in the entire table?
-- Show both in one query
-- Alias them min_budget and max_budget
SELECT MAX(REPLACE(budget, '$', '')::NUMERIC) AS max_budget,
    MIN(REPLACE(budget, '$', '')::NUMERIC) AS min_budget,
FROM jobs;

-- Task 4:
-- What is the total sum of all budgets?
-- AND the average budget
-- BUT only for jobs in your most common category
-- (run SELECT DISTINCT category first to pick one that has many rows)
SELECT SUM(REPLACE(budget, '$', '')::NUMERIC) AS total_budget,
    AVG(REPLACE(budget, '$', '')::NUMERIC) AS avg_budget,
FROM jobs
WHERE category = (SELECT category FROM jobs GROUP BY category ORDER BY COUNT(*) DESC LIMIT 1);

-- Task 5:
-- Write one single query that returns ALL of these together:
-- total_jobs, jobs_with_budget, avg_budget, min_budget, max_budget
-- This is called a summary statistics query
-- Every data engineer writes this on every new dataset they see
SELECT COUNT(*) AS total_jobs,
    COUNT(budget) AS jobs_with_budget,
    ROUND(AVG(REPLACE(budget, '$', '')::NUMERIC), 2) AS avg_budget,
    MIN(REPLACE(budget, '$', '')::NUMERIC) AS min_budget,
    MAX(REPLACE(budget, '$', '')::NUMERIC) AS max_budget
FROM jobs;