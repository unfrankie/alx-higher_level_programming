-- Retrieve all shows with their corresponding genres or NULL if no genre is linked
SELECT tv_shows.title, IFNULL(tv_genres.name, 'NULL') AS name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title, name;
