# Write your MySQL query statement below
WITH Until_date AS (
    SELECT product_id, MAX(change_date) AS last_change
    FROM Products AS p1
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)
SELECT
    p.product_id, new_price AS price
FROM
    Products AS p
JOIN
    Until_date AS u
ON
    p.product_id = u.product_id AND p.change_date = u.last_change
UNION
SELECT DISTINCT p2.product_id, 10
FROM Products AS p2
WHERE p2.product_id NOT IN (
    SELECT product_id
    FROM Until_date
)