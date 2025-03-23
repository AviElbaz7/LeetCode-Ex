# Write your MySQL query statement below
WITH first_year_sold_for_each_product AS (
    SELECT product_id, MIN(year) AS min_year
    FROM Sales
    GROUP BY product_id
)

SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN (
    SELECT product_id, min_year
    FROM first_year_sold_for_each_product
)