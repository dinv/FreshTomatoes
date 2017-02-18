from media import Movie
import fresh_tomatoes

# movie titles to be queried in the database
movie_input = ['Power Rangers', 'Lego Batman', 'Room', 'The Babadook',
               'The Imitation Game', 'The Italian Job', 'Finding Dory',
               'Crazy Stupid Love', 'The Princess Bride']

# generate list of movies
movies = []
for each_movie in movie_input:
    movies.append(Movie(each_movie))

# launch the fresh tomatoes webpage
fresh_tomatoes.open_movies_page(movies)
