--script that lists all shows by rate
--script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv_genres.name AS `name`, SUM(tv_show_ratings.rate) AS `rating`
FROM tv_genres
JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.id
ORDER BY rating DESC;