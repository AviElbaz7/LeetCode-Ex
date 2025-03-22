# Write your MySQL query statement below
WITH categorized_bank_accounts AS (
    SELECT
    SUM(IF(income < 20000, 1, 0)) AS low_salary,
    SUM(IF(income BETWEEN 20000 AND 50000, 1, 0)) AS average_salary,
    SUM(IF(income > 50000, 1, 0)) AS high_salary
    FROM
    Accounts
)
SELECT
    'Low Salary' AS category, low_salary AS accounts_count
FROM
    categorized_bank_accounts
UNION ALL
SELECT
    'Average Salary' AS category, average_salary AS accounts_count
FROM
    categorized_bank_accounts
UNION ALL
SELECT
    'High Salary' AS category, high_salary AS accounts_count
FROM
    categorized_bank_accounts