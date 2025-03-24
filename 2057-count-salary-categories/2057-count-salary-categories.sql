# Write your MySQL query statement below
WITH high_accounts AS (
    SELECT *
    FROM Accounts
    WHERE income > 50000
),
average_accounts AS (
    SELECT *
    FROM Accounts
    WHERE income BETWEEN 20000 AND 50000
),
low_accounts AS (
    SELECT *
    FROM Accounts
    WHERE income < 20000
)

SELECT "High Salary" AS category, IFNULL(COUNT(*), 0) AS accounts_count
FROM high_accounts
UNION ALL
SELECT "Low Salary" AS category, IFNULL(COUNT(*), 0) AS accounts_count
FROM low_accounts
UNION ALL
SELECT "Average Salary" AS category, IFNULL(COUNT(*), 0) AS accounts_count
FROM average_accounts