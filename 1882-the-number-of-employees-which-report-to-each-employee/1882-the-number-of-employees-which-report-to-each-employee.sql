# Write your MySQL query statement below
SELECT
    managers.employee_id,
    managers.name,
    COUNT(workers.reports_to) AS reports_count,
    ROUND(AVG(workers.age)) AS average_age
FROM
    Employees AS managers
JOIN
    Employees AS workers
ON
    managers.employee_id = workers.reports_to
GROUP BY
    managers.employee_id
HAVING
    COUNT(workers.reports_to) >= 1
ORDER BY
    managers.employee_id