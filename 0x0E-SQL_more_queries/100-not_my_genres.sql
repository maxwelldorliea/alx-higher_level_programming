-- lists all genres of the show Dexter

SELECT tv_genres.name FROM tv_genres,tv_shows, tv_show_genres WHERE tv_genres.id = tv_show_genres.genre_id AND tv_shows.id = tv_show_genres.show_id AND tv_shows.title != "Dexter" GROUP BY tv_genres.name ORDER BY tv_genres.name;
