# Write your MySQL query statement below
SELECT m.employee_id, m.name, COUNT(w.reports_to) AS reports_count, ROUND(AVG(w.age), 0) AS average_age
FROM Employees AS w
JOIN Employees AS m
ON w.reports_to = m.employee_id
GROUP BY m.employee_id
ORDER BY m.employee_id