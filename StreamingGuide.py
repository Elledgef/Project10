# Author: Faith Elledge
# Grithubusername: Elledgef
# Date: 5/31
# Description: Created a code that has a Streaming guide
# that will have a list of Streaming services and a dictionary of movies

# movie class
class Movie:
        """ A class to represent a movie.
            title:str
                name of movie
            genre:str
                catagory of movie
            director:str
                who directed the movie
            year:int
                what year was the movie made """
        def __init__(self, title: str, genre: str, director: str, year: int):
            self._title = title
            self._genre = genre
            self._director = director
            self._year = year


        def get_title(self):
            """ Will return the movie title of the movie"""
            return self._title

        def get_genre(self):
            """ Will return the genre of the movie"""
            return self._genre

        def get_director(self):
            """Will return the director of the movie"""
            return self._director

        def get_year(self):
            """Will return the year the movie was made """
            return self._year

    # streaming class
class StreamingService:
        """ A class to represent streaming services that are avalible
            name
                name of streaming service """

        def __init__(self, name):
            self._name = name
            self._catalog = {}

        # get
        def get_name(self):
            """ Will return the name of the service"""
            return self._name

        def get_catalog(self):
            """ will return the catalog of services that are avalible"""
            return self._catalog

        def add_movie(self,movie:Movie):
            """ This allows a movie titles to be added """
            movie_title = movie.get_title()
            self._catalog[movie_title] = movie

        def delete_movie(self, movie_title):
             """ This allows a movie title to be deleted """
             self._catalog.pop(movie_title)

class Streamingguide:
        """ A class to represent a streaming guide that has streaming services and movies"""

        def __init__(self):
            """ Empty list that services will be added to """
            self._services = []
        def add_streaming_service(self,service:StreamingService):
            """ Using this youre able to add a streaming service """
            self._services.append(service)

        def delete_streaming_services(self,serviceName):
            """ Using this to be able to delete a streaming service """
            for i,service in enumerate(self._service):
                if service.get_name()==serviceName:
                    del self._services[i]
                return

        def where_to_watch(self,movie_title):
            """ This allows one to look up a movie title and see if its avalible on streaming services """
            ret_val = []
            movie_year = NA

            for service in self._services:
                if service_catalog().get(movie_title) is not None:
                    movie_year = service.get_catalog()[movie_title].get_year()
                    ret_val.append(service.get_name())
                if movie_year is not None:
                     continue
                return None














