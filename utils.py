from pymongo import MongoClient
import requests


from pymongo import MongoClient
import requests


def set_members_db():
    url = "https://jsonplaceholder.typicode.com/users"

    resp = requests.get(url)
    members = resp.json()
    client = MongoClient(port=27017)
    db = client["subscriptionsDB"]
    collection = db["members"]

    all_db_members = list(collection.find({}))

    if len(all_db_members) == 0:
        for m in members:
            obj = {"name": m["name"], "email": m["email"],
                   'city': m["address"]["city"]}
            collection.insert_one(obj)
    else:
        pass


# o _id(ObjectId)
# o Name
# o Genres(Array od Strings)
# o Image(A string – The url of the image picture)
# o Premiered(Date)
def set_movies_db():
    url = "https://api.tvmaze.com/shows"

    resp = requests.get(url)
    movies = resp.json()
    client = MongoClient(port=27017)
    db = client["subscriptionsDB"]
    collection = db["movies"]

    all_db_movies = list(collection.find({}))

    if len(all_db_movies) == 0:
        for m in movies:
            obj = {'name': m['name'], "genres": m["genres"],
                   "image": m["image"]["medium"], "premiered": m["premiered"]}
            collection.insert_one(obj)
    else:
        pass
