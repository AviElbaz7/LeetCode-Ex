# Write your MySQL query statement below
WITH requesters_num_friends AS (
    SELECT requester_id, COUNT(*) AS friends_num
    FROM RequestAccepted
    GROUP BY requester_id
),
accepters_num_friends AS (
    SELECT accepter_id, COUNT(*) AS friends_num
    FROM RequestAccepted
    GROUP BY accepter_id
),
united AS (
    SELECT id, SUM(friends_num) AS num
    FROM (
        SELECT requester_id AS id, friends_num
        FROM requesters_num_friends
        UNION ALL
        SELECT accepter_id AS id, friends_num
        FROM accepters_num_friends
    ) AS sub
    GROUP BY id
)

SELECT id, num
FROM united
WHERE num = (SELECT MAX(num) FROM united)