-- Task 1:
-- Assign ROW_NUMBER to all jobs ordered by budget DESC
-- Show title, budget, row_num
-- Exclude NULL budgets
-- Use NULLS LAST

SELECT title, budget,
    ROW_NUMBER() OVER(
        ORDER BY REPLACE(budget, '$', ''):: NUMERIC DESC NULLS LAST
    ) AS row_num
FROM jobs
WHERE budget IS NOT NULL;

-- Task 2:
-- Rank all jobs by budget DESC using RANK()
-- Then rank again using DENSE_RANK()
-- Show title, budget, rank, dense_rank in ONE query
-- Where do they differ? Write the answer as a comment

SELECT title, budget,
       DENSE_RANK() OVER(
           ORDER BY REPLACE(budget, '$', '')::NUMERIC DESC NULLS LAST
       ) AS dense_rnk,
       RANK() OVER(
           ORDER BY REPLACE(budget, '$', '')::NUMERIC DESC NULLS LAST
       ) AS rnk
FROM jobs
WHERE budget IS NOT NULL;


-- Task 3:
-- Rank jobs by budget within each category (PARTITION BY category)
-- Use RANK()
-- Show title, category, budget, rank_in_category
-- Exclude NULL budgets

SELECT title, category, budget,
    RANK() OVER(
        PARTITION BY category
        ORDER BY REPLACE(budget, '$', '')::NUMERIC DESC NULLS LAST
    )AS rank_in_category
FROM jobs
WHERE budget IS NOT NULL;

-- Task 4:
-- Find the single top-paying job in each category
-- Use a CTE with RANK() + PARTITION BY
-- Then filter WHERE rank = 1 in the outer query
-- Show title, category, budget

WITH ranked_jobs AS (
    SELECT title, category, budget,
        RANK() OVER(
            PARTITION BY category
            ORDER BY REPLACE(budget, '$', '')::NUMERIC DESC NULLS LAST
        ) AS rank_in_category
    FROM jobs
    WHERE budget IS NOT NULL
)
SELECT title, category, budget
FROM ranked_jobs
WHERE rank_in_category = 1;

-- Task 5:
-- Show each job's budget alongside:
--   overall_avg: average budget across ALL jobs
--   category_avg: average budget within its category
-- Round both to 2 decimal places
-- This shows how each job compares to both global and category averages
-- Exclude NULL budgets

SELECT title, category, budget,
       ROUND(AVG(REPLACE(budget, '$', '')::NUMERIC) OVER(), 2) AS overall_avg,
       ROUND(AVG(REPLACE(budget, '$', '')::NUMERIC) OVER(PARTITION BY category), 2) AS category_avg
FROM jobs
WHERE budget IS NOT NULL;