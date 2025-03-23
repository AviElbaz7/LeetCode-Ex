# Write your MySQL query statement below
WITH managers_of_5_employees AS (
    SELECT managerId
    FROM Employee
    GROUP BY managerId
    HAVING COUNT(*) >= 5
)

SELECT name
FROM Employee
WHERE id IN (
    SELECT managerId
    FROM managers_of_5_employees
)