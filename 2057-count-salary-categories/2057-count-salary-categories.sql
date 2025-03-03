# Write your MySQL query statement below
SELECT
    "Low Salary" AS category, COUNT(account_id) AS accounts_count
FROM
    Accounts AS a
WHERE
    income < 20000
UNION
SELECT
    "Average Salary" AS category, COUNT(account_id) AS accounts_count
FROM
    Accounts AS a
WHERE
    income BETWEEN 20000 AND 50000
UNION
SELECT
    "High Salary" AS category, COUNT(account_id) AS accounts_count
FROM
    Accounts AS a
WHERE
    income > 50000