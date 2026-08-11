-- Task 1:
-- Count how many jobs exist per category
-- Show category and job_count
-- Sort by job_count highest first
SELECT category, COUNT(*) AS job_count
FROM jobs
GROUP BY category
ORDER BY job_count DESC;

-- Task 2:
-- Average budget per category
-- Round to 2 decimal places
-- Sort by avg_budget highest first, NULLS LAST

SELECT category,
    ROUND(AVG(REPLACE(budget, '$', '')::NUMERIC), 2) AS avg_budget
FROM jobs
GROUP BY category
ORDER BY avg_budget DESC NULLS LAST;

-- Task 3:
-- Show only categories that have MORE than 3 jobs
-- Show category and job_count

SELECT category, COUNT(*) AS job_count
FROM jobs
GROUP BY category
HAVING COUNT(*) > 3
ORDER BY job_count DESC;

-- Task 4:
-- Show category, job_count, avg_budget
-- BUT only for rows where budget is NOT NULL (use WHERE)
-- AND only for categories with more than 2 jobs (use HAVING)
-- Sort by avg_budget DESC NULLS LAST

SELECT category, COUNT(*) AS job_count,
    AVG(REPLACE(budget, '$', '')::NUMERIC) AS avg_budget
FROM jobs
WHERE budget IS NOT NULL
GROUP BY category
HAVING COUNT(*) > 2
ORDER BY avg_budget DESC NULLS LAST;

-- Task 5:
-- Group by BOTH category AND experience
-- Count jobs in each combination
-- Sort by category ASC, then job_count DESC

SELECT category, experience, COUNT(*) AS job_count
FROM jobs
GROUP BY category, experience
ORDER BY category ASC, job_count DESC;