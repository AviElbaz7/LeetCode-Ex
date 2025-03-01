# Write your MySQL query statement below
SELECT
    user_id,
    IFNULL(COUNT(DISTINCT follower_id), 0) AS followers_count
FROM
    Followers
GROUP BY
    user_id