# FreshTomatoes
FreshTomatoes is a miniature project that generates a webpage with movie titles, posters, and trailers.  
Code is written using Python, and utilizes [The Movie Database (TMDb) API v3](https://www.themoviedb.org/documentation/api).  
Created for the Full Stack Web Developer nanodegree program with Udacity.

##Setup
0) Clone this repository  
1) Ensure that Python 3 is installed  
2) Install the [tmdbsimple](https://github.com/celiao/tmdbsimple) library  
4) Install the configparser library  
6) [Sign up](https://www.themoviedb.org/account/signup) with The Movie Database, and retrieve an API key  
5) Rename ```config.ini.example``` to ```config.ini```  
6) Place your API key into ```config.ini```  

##Usage
1) Run ```entertainment_center.py```  
2) Change which movies are listed by modifying the ```movie_input``` list in ```entertainment_center.py```   
3) Rerun ```entertainment_center.py``` to see the changes reflected

##QueryHelper
By default, the first result of a query is used.  This can be problematic if the desired movie is not the first result.  

For example, if we wanted to query for 'The Lego Movie', the first result returned is 'The Lego Batman Movie'.  

This can be handled using the QueryHelper utility class, which can assist users in manually verifying a movie ID.  
The ID can then be used in place of a string title in the ```movie_input``` variable.  

Run ```helper_example.py``` to see this illustrated.   
Then, in ```entertainment_center.py```, replace 'Lego Batman' with 137106 to see this reflected on the webpage.
