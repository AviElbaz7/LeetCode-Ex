# Write your MySQL query statement below
WITH employees_with_one_department AS (
    SELECT employee_id, MIN(department_id) AS department_id
    FROM Employee
    GROUP BY employee_id
    HAVING COUNT(department_id) = 1
),
employees_with_more_departments AS (
    SELECT employee_id, department_id
    FROM Employee
    WHERE primary_flag = 'Y'
)

SELECT *
FROM employees_with_one_department
UNION ALL
SELECT *
FROM employees_with_more_departments