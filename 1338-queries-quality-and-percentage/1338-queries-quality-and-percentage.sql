# Write your MySQL query statement below
SELECT
    query_name,
    ROUND(IFNULL(AVG(rating / position), 0), 2) AS quality,
    ROUND(IFNULL(100* (SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END)) / COUNT(*), 0), 2) AS poor_query_percentage
FROM
    Queries AS q
GROUP BY
    query_name