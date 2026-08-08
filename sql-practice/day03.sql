-- Task 1: Jobs in 'Automation' category
-- AND experience is 'Entry Level'
SELECT * FROM jobs
WHERE category = 'Automation'
AND experience = 'Entry';

-- Task 2: Jobs where category is 'Web Development'
-- OR category is 'Data Analyst'
SELECT * FROM jobs
WHERE category = 'Web Development'
OR category = 'Data Analyst';

-- Task 3: All jobs where category is NOT 'Web Development'
SELECT * FROM jobs
WHERE category != 'Web Development'

-- Task 4: Jobs where budget (cast to NUMERIC) is BETWEEN 200 AND 2000
-- AND title contains the word 'developer' (case insensitive)
SELECT * FROM jobs
WHERE REPLACE(budget, '$', '')::NUMERIC BETWEEN 200 AND 2000;

-- Task 5: Jobs where category is IN at least 3 categories of your choice
-- AND title ILIKE contains any keyword you pick
SELECT * FROM jobs
WHERE category IN ('Web Development', 'Automation', 'Data Analyst')
AND title ILIKE '%developer%';