# Write your MySQL query statement below
WITH fisrt_orders AS (
    SELECT *
    FROM Delivery AS d1
    WHERE order_date = (SELECT MIN(order_date) FROM Delivery AS d2 WHERE d1.customer_id = d2.customer_id)
)
SELECT
    ROUND(AVG(IF(order_date = customer_pref_delivery_date, 1, 0)) * 100, 2) AS immediate_percentage
FROM
    fisrt_orders