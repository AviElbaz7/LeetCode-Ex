# Write your MySQL query statement below
SELECT
    manager.name
FROM
    Employee AS employee
JOIN
    Employee AS manager
ON
    employee.managerId = manager.id
GROUP BY
    manager.id
HAVING
    COUNT(employee.id) >= 5