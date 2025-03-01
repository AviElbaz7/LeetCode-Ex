# Write your MySQL query statement below
SELECT
    ROUND(IFNULL(COUNT(DISTINCT a.player_id) / (SELECT COUNT(DISTINCT a3.player_id) FROM Activity AS a3), 0), 2) AS fraction
FROM
    Activity AS a
WHERE (a.player_id, DATE_ADD(a.event_date, INTERVAL -1 DAY)) IN (
    SELECT sub.player_id, MIN(sub.event_date)
    FROM Activity AS sub
    GROUP BY sub.player_id
)