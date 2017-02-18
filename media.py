import tmdbsimple as tmdb
from configparser import SafeConfigParser

#grab TMDb API key from config.ini
parser = SafeConfigParser()
parser.read('config.ini')
tmdb.API_KEY = parser.get('TMDb API Key','key')

class Movie():
    """
    This class provides a way to store movie related information.
    It utilizes the tmdbsimple library, a wrapper for The Movie Database (TMDb) API v3
    """

    # obtain configuration info from TMDb to generate poster URLs
    conf = tmdb.Configuration()
    reponse = conf.info()

    # object for querying the database
    search = tmdb.Search()

    # class variables
    YOUTUBE_BASE_URL = 'https://www.youtube.com/watch?v='
    POSTER_SECURE_BASE_URL = conf.images['secure_base_url']
    POSTER_SIZE = 'w342'

    def __init__(self, title):
        self.movie = tmdb.Movies(self.get_movie_id(title))
        self.title = self.get_movie_title()
        self.poster_image_url = self.POSTER_SECURE_BASE_URL + \
            self.POSTER_SIZE + self.get_poster_path()
        self.trailer_youtube_url = self.YOUTUBE_BASE_URL + self.get_youtube_key()

    def get_movie_id(self, title):
        '''Returns the movie ID for a given title query'''
        reponse = self.search.movie(query=title)
        return self.search.results[0]['id']

    def get_movie_title(self):
        '''Returns the movie title from the database for a given title query'''
        return self.search.results[0]['title']

    def get_youtube_key(self):
        '''Returns the YouTube key for the movie trailer'''
        response = self.movie.videos()
        return self.movie.results[0]['key']

    def get_poster_path(self):
        '''Returns the poster path for the movie poster'''
        response = self.movie.images()
        return self.movie.posters[0]['file_path']
