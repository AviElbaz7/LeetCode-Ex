# Write your MySQL query statement below
SELECT author_id AS id
FROM Views
GROUP BY author_id, viewer_id
HAVING COUNT(*) >= 1 AND author_id = viewer_id
ORDER BY author_id ASC