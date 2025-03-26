# Write your MySQL query statement below
# requester friends
WITH requester_friends AS (
    SELECT requester_id, COUNT(*) AS num_of_friends
    FROM RequestAccepted
    GROUP BY requester_id
),
accepter_friends AS (
    SELECT accepter_id, COUNT(*) AS num_of_friends
    FROM RequestAccepted
    GROUP BY accepter_id
),
all_friends AS (
    SELECT id, SUM(num) AS num
    FROM
    (
        SELECT requester_id AS id, num_of_friends AS num
        FROM requester_friends
        UNION ALL
        SELECT *
        FROM accepter_friends
    ) AS sub
    GROUP BY id
)

SELECT *
FROM all_friends
WHERE num = (SELECT MAX(num) FROM all_friends)