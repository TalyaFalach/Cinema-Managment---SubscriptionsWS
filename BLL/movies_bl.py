from DAL.movies_dal import MoviesDAL


class MoviesBL:
    def __init__(self):
        self.__movies = MoviesDAL()

    def get_all_movies(self):
        movies = self.__movies.get_all_movies()
        return movies

    def get_movie(self, id):
        movie = self.__movies.get_movie(id)
        return movie

    def add_movie(self, obj):
        movie = self.__movies.add_movie(obj)
        return movie

    def update_movie(self, id, obj):
        movie = self.__movies.update_movie(id, obj)
        return movie

    def delete_movie(self, id):
        movie = self.__movies.delete_movie(id)
        return movie
