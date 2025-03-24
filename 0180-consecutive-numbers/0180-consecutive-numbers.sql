# Write your MySQL query statement below
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT *,
    COUNT(*) OVER (ORDER BY id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS cnt,
    MAX(num) OVER (ORDER BY id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS max_val,
    MIN(num) OVER (ORDER BY id ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS min_val
    FROM Logs
) AS windowed
WHERE cnt = 3 AND max_val = min_val