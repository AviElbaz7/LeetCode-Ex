# Write your MySQL query statement below
WITH first_orders AS (
    SELECT customer_id, MIN(order_date) AS min_order_date
    FROM Delivery
    GROUP BY customer_id
)

SELECT ROUND(IFNULL(100 * AVG(IF(order_date = customer_pref_delivery_date, 1, 0)), 0), 2) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, min_order_date
    FROM first_orders
)