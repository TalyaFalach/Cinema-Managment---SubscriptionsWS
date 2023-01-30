from flask import Flask
from bson import ObjectId
from flask_cors import CORS
import json
from utils import set_members_db, set_movies_db
from routers.members_router import members
from routers.movies_router import movies
from routers.subscriptions_router import subscriptions
app = Flask(__name__)

app.url_map.strict_slashes = False

class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return json.JSONEncoder.default(self, obj)


app.json_encoder = JSONEncoder

CORS(app)


app.register_blueprint(members, url_prefix='/members')
app.register_blueprint(movies, url_prefix='/movies')
app.register_blueprint(subscriptions, url_prefix='/subscriptions')
set_members_db()
set_movies_db()
app.run(host="0.0.0.0", port=5001)