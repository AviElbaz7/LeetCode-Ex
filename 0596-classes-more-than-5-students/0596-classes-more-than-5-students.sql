# Write your MySQL query statement below
SELECT
    class
FROM
    Courses AS c
GROUP BY
    class
HAVING
    COUNT(*) >= 5