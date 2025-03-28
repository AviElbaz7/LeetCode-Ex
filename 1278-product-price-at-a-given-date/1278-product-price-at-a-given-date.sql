# Write your MySQL query statement below
WITH last_date_per_product AS (
    SELECT product_id, MAX(change_date) AS last_date
    FROM Products
    WHERE change_date <= '2019-08-16'
    GROUP BY product_id
)

SELECT DISTINCT product_id, 10 AS price
FROM Products
WHERE product_id NOT IN (SELECT product_id FROM last_date_per_product)
UNION ALL
SELECT DISTINCT product_id, new_price
FROM Products
WHERE (product_id, change_date) IN (SELECT product_id, last_date FROM last_date_per_product)