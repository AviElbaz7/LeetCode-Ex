# Write your MySQL query statement below
-- WITH num_of_unique_products_per_customer AS (
--     SELECT customer_id
--     FROM Customer
--     GROUP BY customer_id
--     HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) AS num FROM Product)
-- )

SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) AS num FROM Product)