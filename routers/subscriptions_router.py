from flask import jsonify, Blueprint, request, make_response
from BLL.subscriptions_bl import SubscriptionsBL


subscriptions_bl = SubscriptionsBL()
subscriptions = Blueprint("subscriptions", __name__)

# GET All


@subscriptions.route('/', methods=['GET'])
def get_all_subscriptions():
    subscriptions = subscriptions_bl.get_all()
    return jsonify(subscriptions)


@subscriptions.route('/<id>', methods=['GET'])
def get_by_id(id):
    subscription = subscriptions_bl.get_by_id(id)
    return jsonify(subscription)


@subscriptions.route('/', methods=['POST'])
def create_subscription():
    memberId = request.json["memberId"]

    movieId = request.json["movieId"]
    date = request.json["date"]
    obj = {"memberId": memberId, "movies": [
        {"movieId": movieId, "date": date}]}

    subscription = subscriptions_bl.create_subscription(obj)
    return jsonify(subscription)


@subscriptions.route('/<id>', methods=['POST'])
def add_to_exist_subscription(id):
    movie = {"movieId": request.json["movieId"], "date": request.json["date"]}
    result = subscriptions_bl.add_to_exist_subscription(id, movie)
    return jsonify(result)
