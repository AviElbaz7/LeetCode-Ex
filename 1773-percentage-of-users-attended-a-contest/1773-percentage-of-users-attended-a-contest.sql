# Write your MySQL query statement below
SELECT
    contest_id,
    ROUND(IFNULL(100*COUNT(DISTINCT r.user_id)/(SELECT COUNT(*) FROM Users), 0), 2) AS percentage
FROM
    Register AS r
GROUP BY
    contest_id
ORDER BY
    percentage DESC, contest_id ASC