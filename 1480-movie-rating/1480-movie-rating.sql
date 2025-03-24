WITH user_rating_count AS (
    SELECT user_id, COUNT(*) AS rating_count
    FROM MovieRating
    GROUP BY user_id
),
top_user AS (
    SELECT u.name
    FROM Users u
    JOIN user_rating_count ur ON u.user_id = ur.user_id
    WHERE ur.rating_count = (
        SELECT MAX(rating_count) FROM user_rating_count
    )
    ORDER BY u.name
    LIMIT 1
),
movie_avg_rating AS (
    SELECT movie_id, AVG(rating) AS avg_rating
    FROM MovieRating
    WHERE YEAR(created_at) = 2020 AND MONTH(created_at) = 2
    GROUP BY movie_id
),
top_movie AS (
    SELECT m.title
    FROM Movies m
    JOIN movie_avg_rating r ON m.movie_id = r.movie_id
    WHERE r.avg_rating = (
        SELECT MAX(avg_rating) FROM movie_avg_rating
    )
    ORDER BY m.title
    LIMIT 1
)

SELECT name AS results FROM top_user
UNION ALL
SELECT title FROM top_movie;
