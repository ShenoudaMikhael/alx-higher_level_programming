-- lists all genres of the show NOT Dexter.
-- script that uses the hbtn_0d_tvshows database to lists all genres of the show NOT Dexter.
SELECT tv_genres.name
FROM tv_genres
JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_show_genres.show_id = (SELECT tv_shows.id FROM tv_shows WHERE tv_shows.title = 'Dexter');