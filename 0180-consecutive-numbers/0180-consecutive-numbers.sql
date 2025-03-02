# Write your MySQL query statement below
SELECT
    DISTINCT l1.num AS ConsecutiveNums
FROM
    Logs AS l1
JOIN
    Logs AS l2
ON
    l1.num = l2.num AND l2.id = 1 + l1.id
JOIN
    Logs AS l3
ON
    l2.num = l3.num AND l3.id = 1 + l2.id