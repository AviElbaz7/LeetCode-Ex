# Write your MySQL query statement below
SELECT
    x, y, z, 'Yes' AS triangle
FROM
    Triangle AS t
WHERE
    (x + y > z) AND (x + z > y) AND (y + z > x)
UNION
SELECT
    x, y, z, 'No' AS triangle
FROM
    Triangle AS t1
WHERE
    (x + y <= z) OR (x + z <= y) OR (y + z <= x)