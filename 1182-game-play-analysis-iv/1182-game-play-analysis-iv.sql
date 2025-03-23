# Write your MySQL query statement below
WITH first_login AS (
    SELECT player_id, MIN(event_date) AS min_date
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND(COUNT(DISTINCT a.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM Activity AS a
JOIN first_login AS f
ON a.player_id = f.player_id AND a.event_date = DATE_ADD(f.min_date, INTERVAL 1 DAY)