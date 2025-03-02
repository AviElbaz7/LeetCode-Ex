# Write your MySQL query statement below
SELECT
    person_name
FROM (
    SELECT person_name, weight, SUM(weight) OVER(ORDER BY turn) AS running_total
    FROM Queue
) AS temp_table
WHERE
    running_total <= 1000
ORDER BY
    running_total DESC
LIMIT
    1