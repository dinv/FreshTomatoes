from media import Movie, QueryHelper

bad = Movie('The Lego Movie')
# not exactly what we wanted
print('')
print("bad = Movie('The Lego Movie')")
print("bad.title is", bad.title)

print('')
print('QueryHelper results:')
q = QueryHelper('The Lego Movie')
'''
prints the following:
    The Lego Batman Movie 324849
    The Lego Movie 137106
    The LEGO Ninjago Movie 274862
    The Lego Movie Sequel 280217
    Lego Batman: The Movie - DC Super Heroes Unite 177271
    The LEGO Movie 4D: A New Adventure 381123
    Lego Legends of Chima 4D Movie Experience 295348
    Mr Peabody and The lego movie 417925
'''

print('')
good = Movie(137106)
# the correct movie title and other data is attained
print("good = Movie(137106)")
print("good.title is", good.title)
print('')
