-- Task 1:
-- Return all jobs sorted by budget highest to lowest
-- Cast budget to NUMERIC before sorting
SELECT * FROM jobs
ORDER BY REPLACE(budget, '$', '')::NUMERIC DESC;

-- Task 2:
-- Return only the top 3 highest budget jobs
-- Show title and budget only
SELECT title, budget FROM jobs
ORDER BY REPLACE(budget, '$', '')::NUMERIC DESC LIMIT 3;


-- Task 3:
-- Return unique list of all categories in your dataset
-- Sort them alphabetically A to Z
SELECT DISTINCT category FROM jobs
ORDER BY category;

-- Task 4:
-- Return top 5 jobs sorted by budget descending
-- BUT skip the first 2 rows (use OFFSET)
-- Think: what is this simulating in a real app?
SELECT * FROM jobs
ORDER BY REPLACE(budget, '$', '')::NUMERIC DESC LIMIT 5 OFFSET 2;


-- Task 5:
-- Return all jobs sorted by category ASC first
-- then by budget DESC within each category
-- Show title, category, budget
SELECT title, category, budget FROM jobs
ORDER BY category,
    REPLACE(budget, '$', '')::NUMERIC DESC;