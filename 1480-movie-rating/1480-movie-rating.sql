# Write your MySQL query statement below

# name of user who watched most movies
WITH num_movies_user_watched AS (
    SELECT name
    FROM MovieRating AS mr
    NATURAL JOIN Users AS u
    GROUP BY user_id
    ORDER BY COUNT(DISTINCT movie_id) DESC, name
    LIMIT 1
),
# average rating of each movie for february 2020
average_rating_per_movie AS (
    SELECT title
    FROM MovieRating
    NATURAL JOIN Movies
    WHERE YEAR(created_at) = 2020 AND MONTH(created_at) = 2
    GROUP BY movie_id
    ORDER BY AVG(rating) DESC, title
    LIMIT 1
)

SELECT name AS results FROM num_movies_user_watched
UNION ALL
SELECT title FROM average_rating_per_movie