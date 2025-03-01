# Write your MySQL query statement below
SELECT
    ROUND(IFNULL(100*SUM(CASE WHEN DATEDIFF(customer_pref_delivery_date, order_date) = 0 THEN 1 ELSE 0 END) / COUNT(order_date), 0), 2) AS immediate_percentage
FROM
    Delivery
WHERE
    (customer_id, order_date) IN (
        SELECT customer_id, MIN(order_date)
        FROM Delivery
        GROUP BY customer_id
    )