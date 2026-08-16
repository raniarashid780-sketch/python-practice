-- Task 1:
-- Find all jobs where budget is above the overall average budget
-- Write it as a SUBQUERY in WHERE first
-- Then rewrite the EXACT same query as a CTE
-- Both must return identical results

-- SUBQUERY
SELECT title, budget
FROM jobs
WHERE REPLACE(budget, '$', '')::NUMERIC >(
    SELECT AVG(REPLACE(budget, '$', '')::NUMERIC)
    FROM jobs
    WHERE budget IS NOT NULL
)
ORDER BY REPLACE(budget, '$', '')::NUMERIC DESC NULLS LAST;

--CTE
WITH avg_budget AS (
    SELECT AVG(REPLACE(budget, '$', '')::NUMERIC) AS avg
    FROM jobs
    WHERE budget IS NOT NULL
)
SELECT j.title, j.budget
FROM jobs j, avg_budget a
WHERE REPLACE(j.budget, '$', '')::NUMERIC > a.avg
ORDER BY REPLACE(j.budget, '$', '')::NUMERIC DESC NULLS LAST;

-- Task 2:
-- Find the single highest budget job using a subquery
-- Show title, category, budget
-- Do NOT use ORDER BY + LIMIT 1 — use a subquery with MAX()

SELECT title, category, budget
FROM jobs
WHERE REPLACE(budget, '$', '')::NUMERIC = (
    SELECT MAX(REPLACE(budget, '$', '')::NUMERIC)
    FROM jobs
    WHERE budget IS NOT NULL
);

-- Task 3:
-- Use a subquery in FROM to find categories
-- where average budget is above 300
-- Show category and avg_budget rounded to 2 decimal places

SELECT category, avg_budget
FROM (
    SELECT category,
        ROUND(AVG(REPLACE(budget, '$', '')::NUMERIC), 2) AS avg_budget
    FROM jobs
    WHERE budget IS NOT NULL
    GROUP BY category
) AS cat_avg
WHERE avg_budget > 300;

-- Task 4:
-- Write a CTE called clean_jobs that:
--   removes NULL budgets
--   converts budget to NUMERIC (strip the $)
-- Then use that CTE to find the top 3 categories by average budget
-- Show category and avg_budget

WITH clean_jobs AS (
    SELECT title, category,
        REPLACE(budget, '$', '')::NUMERIC AS budget
    FROM jobs
    WHERE budget IS NOT NULL
),
category_stats AS(
    SELECT category,
        ROUND(AVG(budget), 2) AS avg_budget,
        COUNT(*) AS job_count
    FROM clean_jobs
    GROUP BY category
)
SELECT category, avg_budget
FROM category_stats
ORDER BY avg_budget DESC NULLS LAST
LIMIT 3;

-- Task 5:
-- Write a chained CTE:
--   CTE 1 called clean_jobs: strip $ and cast budget, remove NULLs
--   CTE 2 called category_stats: avg_budget and job_count per category
-- Final SELECT: categories where job_count > 1 AND avg_budget > 200
-- Sort by avg_budget DESC NULLS LAST

WITH clean_jobs AS (
    SELECT title, category,
        REPLACE(budget, '$', '')::NUMERIC AS budget
    FROM jobs
    WHERE budget IS NOT NULL
),
category_stats AS(
    SELECT category,
        ROUND(AVG(budget), 2) AS avg_budget,
        COUNT(*) AS job_count
    FROM clean_jobs
    GROUP BY category
)
SELECT *
FROM category_stats
WHERE job_count > 1 AND avg_budget > 200
ORDER BY avg_budget DESC NULLS LAST;