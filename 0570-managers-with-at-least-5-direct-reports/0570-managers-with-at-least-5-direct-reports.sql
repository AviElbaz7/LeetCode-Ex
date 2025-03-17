# Write your MySQL query statement below
SELECT
    employee.name
FROM
    Employee AS employee
JOIN
    Employee AS manager
ON
    employee.id = manager.managerId
GROUP BY
    manager.managerId
HAVING
    COUNT(*) >= 5