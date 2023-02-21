-- Import the database dump from hbtn_0d_tvshows
-- to your MySQL server: download
-- Write a script that lists all shows contained in hbtn_0d_tvshows
-- that have at least one genre linked.
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ORDER BY tv_shows.title ASC;