# Write your MySQL query statement below
WITH comulative_wheights AS (
    SELECT person_id, person_name, turn, SUM(weight) OVER (ORDER BY turn) AS num_weight
    FROM Queue
)

SELECT person_name
FROM comulative_wheights
WHERE num_weight <= 1000
ORDER BY num_weight DESC
LIMIT 1