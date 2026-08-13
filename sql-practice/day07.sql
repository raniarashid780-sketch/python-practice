-- Task 1:
-- Find all jobs where budget IS NULL
-- Show title and experience

SELECT title, experience
FROM jobs
WHERE budget IS NULL;

-- Task 2:
-- Find all jobs where budget IS NOT NULL
-- Show title, budget, category
-- Sort by category ASC

SELECT title, budget, category
FROM jobs
WHERE budget IS NOT NULL
ORDER BY category ASC;

-- Task 3:
-- Show title and a column called clean_budget
-- where NULL budgets are replaced with '$0' using COALESCE
-- Show ALL rows including previously NULL ones

SELECT title,
    COALESCE(budget, '$0') AS clean_budget
FROM jobs;

-- Task 4:
-- Show title and daily_rate (budget divided by 30)
-- Use COALESCE to treat NULL budget as 0
-- Use table alias 'j' for jobs
-- Round daily_rate to 2 decimal places

SELECT j.title,
    ROUND(COALESCE(REPLACE(j.budget, '$', '')::NUMERIC, 0) / 30, 2) AS daily_rate
FROM jobs j;

-- Task 5:
-- Show category, total_jobs, jobs_with_budget, missing_budget
-- missing_budget = total_jobs minus jobs_with_budget
-- This tells you how many jobs per category have no budget listed
-- Sort by missing_budget DESC

SELECT category,
    COUNT(*) AS total_jobs,
    COUNT(budget) AS jobs_with_budget,
    COUNT(*) - COUNT(budget) AS missing_budget
FROM jobs
GROUP BY category
ORDER BY missing_budget DESC;





