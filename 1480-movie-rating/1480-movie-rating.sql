# Write your MySQL query statement below

# number of movies watched by each user
WITH num_movies_user_watched AS (
    SELECT user_id, COUNT(DISTINCT movie_id) AS num_movies_watched
    FROM MovieRating AS mr
    GROUP BY user_id
),
# average rating of each movie for february 2020
average_rating_per_movie AS (
    SELECT movie_id, AVG(rating) AS avg_rating
    FROM MovieRating
    WHERE YEAR(created_at) = 2020 AND MONTH(created_at) = 2
    GROUP BY movie_id
),
# answer part 1
user_rated_most_movies AS (
    SELECT u.name AS results
    FROM num_movies_user_watched AS n
    JOIN Users AS u
    ON n.user_id = u.user_id
    WHERE n.num_movies_watched = (SELECT MAX(num_movies_watched) FROM num_movies_user_watched)
    ORDER BY name
    LIMIT 1
),
# answer part 2
top_average_rated_movie AS (
    SELECT m1.title AS results
    FROM average_rating_per_movie AS arpm
    JOIN Movies AS m1
    ON arpm.movie_id = m1.movie_id
    WHERE arpm.avg_rating = (SELECT MAX(avg_rating) FROM average_rating_per_movie)
    ORDER BY title
    LIMIT 1
)

SELECT * FROM user_rated_most_movies
UNION ALL
SELECT * FROM top_average_rated_movie