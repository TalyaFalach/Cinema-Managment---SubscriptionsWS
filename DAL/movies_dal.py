from pymongo import MongoClient
from bson import ObjectId


class MoviesDAL:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["subscriptionsDB"]
        self.__collection = self.__db["movies"]

    def get_all_movies(self):
        movies = list(self.__collection.find({}))
        return movies

    def get_movie(self, id):
        movie = self.__collection.find_one({"_id": ObjectId(id)})
        if movie == None:
            return "Movie Not Exist"
        else:
            return movie

    def add_movie(self, obj):
        self.__collection.insert_one(obj)
        return "The Movie '" + str(obj["name"]) + "' Created With ID: " + str(obj["_id"])

    def update_movie(self, id, obj):
        self.__collection.update_one({"_id": ObjectId(id)}, {"$set": obj})
        return "Updated !"

    def delete_movie(self, id):
        self.__collection.delete_one({"_id": ObjectId(id)})
        return "Deleted"
