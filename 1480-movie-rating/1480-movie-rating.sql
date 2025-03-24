# Write your MySQL query statement below
WITH num_rating__for_each_user AS (
    SELECT user_id, COUNT(movie_id) AS num_movies
    FROM MovieRating
    GROUP BY user_id
),
top_users_rated AS (
    SELECT u.name
    FROM num_rating__for_each_user n
    NATURAL JOIN Users u
    WHERE n.num_movies = (SELECT MAX(num_movies) FROM num_rating__for_each_user)
    ORDER BY u.name
    LIMIT 1
),
average_rating_per_movie_in_February_2020 AS (
    SELECT mr.movie_id, AVG(rating) AS ave_rate
    FROM MovieRating AS mr
    WHERE MONTH(mr.created_at) = 2 AND YEAR(mr.created_at) = 2020
    GROUP BY mr.movie_id
),
movie_name_with__highest_average_rating_in_February_2020 AS (
    SELECT m.title
    FROM average_rating_per_movie_in_February_2020 AS ave
    NATURAL JOIN Movies AS m
    WHERE ave.ave_rate = (SELECT MAX(ave_rate) FROM average_rating_per_movie_in_February_2020)
    ORDER BY m.title
    LIMIT 1
)

SELECT title AS results
FROM movie_name_with__highest_average_rating_in_February_2020
UNION ALL
SELECT name
FROM top_users_rated