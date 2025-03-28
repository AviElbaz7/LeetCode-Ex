# Write your MySQL query statement below
WITH first_login_of_players AS (
    SELECT player_id, MIN(event_date) AS min_date
    FROM Activity
    GROUP BY player_id
)

SELECT ROUND(COUNT(*) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM first_login_of_players AS f
JOIN Activity AS a
ON f.player_id = a.player_id AND f.min_date = DATE_SUB(a.event_date, INTERVAL 1 DAY)
