# Write your MySQL query statement below
WITH managers_who_left AS (
    SELECT manager_id
    FROM Employees
    WHERE manager_id NOT IN (SELECT employee_id FROM Employees)
)

SELECT employee_id
FROM Employees
WHERE salary < 30000 AND manager_id IN (SELECT * FROM managers_who_left)
ORDER BY employee_id