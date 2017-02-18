from media import Movie, QueryHelper
import fresh_tomatoes

# movie input
# strings are handled query values
# integers are handled as database ID
movie_input = ['Power Rangers', 'Lego Batman', 'Room', 'The Babadook',
               'The Imitation Game', 'The Italian Job', 'Finding Dory',
               'Crazy Stupid Love', 'The Princess Bride']

# generate list of movies
movies = []
for each in movie_input:
    movies.append(Movie(each))

# launch the fresh tomatoes webpage
fresh_tomatoes.open_movies_page(movies)
