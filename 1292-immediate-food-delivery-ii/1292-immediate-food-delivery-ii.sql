# Write your MySQL query statement below
WITH first_order_of_customers AS (
    SELECT customer_id, MIN(order_date) AS min_date
    FROM Delivery
    GROUP BY customer_id
)

SELECT ROUND(100 * SUM(IF(order_date = customer_pref_delivery_date, 1, 0)) / COUNT(*), 2) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (SELECT customer_id, min_date FROM first_order_of_customers)