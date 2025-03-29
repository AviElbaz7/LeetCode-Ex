# Write your MySQL query statement below
WITH user_that_rated_most_movies AS (
    SELECT m.user_id, u.name
    FROM MovieRating AS m
    NATURAL JOIN Users AS u
    GROUP BY m.user_id, u.name
    ORDER BY COUNT(DISTINCT movie_id) DESC, u.name
    LIMIT 1
),
movie_with_highest_average_rating_in_febuary_2020 AS (
    SELECT mr.movie_id,  m.title
    FROM MovieRating AS mr
    NATURAL JOIN Movies AS m
    WHERE YEAR(mr.created_at) = 2020 AND MONTH(mr.created_at) = 2
    GROUP BY mr.movie_id, m.title
    ORDER BY AVG(mr.rating) DESC, m.title
    LIMIT 1
)

SELECT name AS results
FROM user_that_rated_most_movies
UNION ALL
SELECT title
FROM movie_with_highest_average_rating_in_febuary_2020
