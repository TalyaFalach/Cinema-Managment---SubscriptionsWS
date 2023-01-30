from DAL.subscriptions_dal import SubscriptionsDAL
from DAL.members_dal import MembersDAL
from DAL.movies_dal import MoviesDAL


class SubscriptionsBL:
    def __init__(self):
        self._subscriptions = SubscriptionsDAL()
        self._members = MembersDAL()
        self._movies = MoviesDAL()
        
    def get_all(self):
        subscriptions = self._subscriptions.get_all()
        return subscriptions
    

    def get_by_id(self, id):
        result = self._subscriptions.get_by_id(id)
        return result

    def create_subscription(self, obj):
        result = self._subscriptions.create_subscription(obj)
        return result

    def add_to_exist_subscription(self, id, movie):
        result = self._subscriptions.add_to_exist_subscription(id, movie)
        return result
