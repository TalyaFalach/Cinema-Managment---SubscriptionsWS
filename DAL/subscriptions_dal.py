from pymongo import MongoClient
from bson import ObjectId


class SubscriptionsDAL:
    def __init__(self):
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["subscriptionsDB"]
        self.__collection = self.__db["subscriptions"]

    def get_all(self):
        data = list(self.__collection.find({}))
        return data

    def get_by_id(self, id):
        result = self.__collection.find_one({"memberId": str(id)})
        if result:
            return "exist"
        else:
            return "not exist"

    def create_subscription(self, obj):
        self.__collection.insert_one(obj)
        return "Created"

    def add_to_exist_subscription(self, id, movie):
        self.__collection.update_one(
            {"memberId":str(id)},
            {"$push" : {"movies": movie}}
        )
        return "updated"
        
       
