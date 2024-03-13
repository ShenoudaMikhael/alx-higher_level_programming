--script that lists all shows by rate
--script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv_genres.name, SUM(tv_show_ratings.rate) as rating
FROM tv_shows
JOIN tv_show_ratings on tv_shows.id = tv_show_ratings.show_id
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres on tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.id
ORDER BY rating DESC;