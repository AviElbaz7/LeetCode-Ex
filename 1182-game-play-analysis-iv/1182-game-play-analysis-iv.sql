# Write your MySQL query statement below
# first login
WITH first_login AS (
    SELECT player_id, MIN(event_date) AS first_date
    FROM Activity AS a1
    GROUP BY player_id
)
SELECT
    ROUND(COUNT(DISTINCT f.player_id) / COUNT(DISTINCT a.player_id), 2) AS fraction
FROM
    Activity AS a
LEFT JOIN
    first_login AS f
ON
    a.player_id = f.player_id AND a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY)