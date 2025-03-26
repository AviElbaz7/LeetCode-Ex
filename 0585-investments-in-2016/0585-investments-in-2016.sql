# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE pid IN (
    SELECT i1.pid
    FROM Insurance AS i1
    JOIN Insurance AS i2
    ON i1.pid <> i2.pid AND i1.tiv_2015 = i2.tiv_2015
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)