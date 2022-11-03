-- lists all Comedy shows in the database hbtn_0d_tvshows
SELECT tv_shows.title FROM tv_genres,tv_shows, tv_show_genres WHERE tv_genres.id = tv_show_genres.genre_id AND tv_shows.id = tv_show_genres.show_id AND tv_genres.name = "Comedy" GROUP BY tv_shows.title ORDER BY tv_shows.title;
