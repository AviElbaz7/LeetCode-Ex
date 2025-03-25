SELECT 
    visited_on,
    SUM(amount) AS amount,
    ROUND(SUM(amount) / 7, 2) AS average_amount
FROM (
    SELECT 
        v.visited_on,
        c.amount
    FROM (
        SELECT DISTINCT visited_on FROM Customer
    ) v
    JOIN Customer c 
        ON c.visited_on BETWEEN DATE_SUB(v.visited_on, INTERVAL 6 DAY) AND v.visited_on
) AS sub
GROUP BY visited_on
HAVING DATEDIFF(visited_on, (SELECT MIN(visited_on) FROM Customer)) >= 6
ORDER BY visited_on;
