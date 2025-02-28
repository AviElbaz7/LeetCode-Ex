# Write your MySQL query statement below
SELECT
    *
FROM
    Cinema AS c
WHERE
    description != 'boring' AND MOD(id, 2) != 0
ORDER BY
    rating DESC