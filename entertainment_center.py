from media import Movie, QueryHelper
import fresh_tomatoes

# movie input
# strings are handled as query values
# integers are handled as database ID
movie_input = ['Power Rangers', 'Lego Batman', 'Room', 'The Babadook',
               'The Imitation Game', 'The Italian Job', 'Finding Dory',
               'Crazy Stupid Love', 'The Princess Bride']

# generate list of movies
movies = [Movie(i) for i in movie_input]

# launch the fresh tomatoes webpage
fresh_tomatoes.open_movies_page(movies)
