# assists user in verifying that the first result returned for
# a query is the desired movie
from media import Movie, QueryHelper

movie_input = ['Batman', 'The Lego Movie']

for each in movie_input:
	print ('Query:' + each)
	QueryHelper(each)
