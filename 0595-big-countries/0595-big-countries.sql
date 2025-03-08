# Write your MySQL query statement below
SELECT
    name, area, population
FROM
    World as w
WHERE
    area >= 3000000 or population >= 25000000