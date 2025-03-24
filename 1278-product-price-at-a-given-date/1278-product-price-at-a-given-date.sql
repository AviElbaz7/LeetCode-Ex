# Write your MySQL query statement below
WITH until_2019_08_16 AS (
    SELECT product_id, MAX(change_date) AS last_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)

SELECT DISTINCT product_id, 10 AS price
FROM Products
WHERE product_id NOT IN (SELECT product_id FROM until_2019_08_16)

UNION ALL

SELECT u.product_id, new_price
FROM until_2019_08_16 AS u
JOIN Products AS p
ON u.product_id = p.product_id AND u.last_date = p.change_date