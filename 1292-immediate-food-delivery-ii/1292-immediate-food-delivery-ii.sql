# Write your MySQL query statement below
WITH fisrt_orders AS (
    SELECT customer_id, MIN(order_date) AS first_order
    FROM Delivery AS d1
    GROUP BY customer_id
)
SELECT
    ROUND(AVG(IF(order_date = customer_pref_delivery_date, 1, 0)) * 100, 2) AS immediate_percentage
FROM
    Delivery AS d
JOIN
    fisrt_orders AS f
WHERE
    d.customer_id = f.customer_id AND d.order_date  = f.first_order