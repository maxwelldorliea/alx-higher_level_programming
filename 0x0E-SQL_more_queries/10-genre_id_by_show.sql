-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres, tv_genres, tv_shows WHERE tv_show_genres.show_id = tv_shows.id AND tv_show_genres.genre_id = tv_genres.id ORDER BY tv_shows.title, tv_show_genres.genre_id;
