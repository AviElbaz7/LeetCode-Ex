# Write your MySQL query statement below
WITH comulative_weights_by_turn AS (
    SELECT person_name, SUM(weight) OVER (ORDER BY turn) AS comulative
    FROM Queue
)

SELECT person_name
FROM comulative_weights_by_turn
WHERE comulative = (SELECT MAX(comulative) AS new FROM comulative_weights_by_turn WHERE comulative <= 1000)