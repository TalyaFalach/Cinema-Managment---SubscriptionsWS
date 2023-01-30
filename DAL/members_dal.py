import requests
from pymongo import MongoClient
from bson import ObjectId


class MembersDAL:
    def __init__(self):
        self.__url = "https://jsonplaceholder.typicode.com/users"
        self.__client = MongoClient(port=27017)
        self.__db = self.__client["subscriptionsDB"]
        self.__collection = self.__db["members"]

    def get_all_members(self):
        members = list(self.__collection.find({}))
        return members

    def get_member(self, id):
        member = self.__collection.find_one({"_id": ObjectId(id)})
        if member == None:
            return "Member Not Exist"
        else:
            return member

    def add_member(self, obj):
        self.__collection.insert_one(obj)
        return  str(obj["_id"])

    def update_member(self, id, obj):
        self.__collection.update_one({"_id": ObjectId(id)}, {"$set": obj})
        return "Updated !"

    def delete_member(self, id):
        self.__collection.delete_one({"_id": ObjectId(id)})
        return "Deleted"
