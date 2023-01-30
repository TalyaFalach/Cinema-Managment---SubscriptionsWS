from flask import jsonify, Blueprint, request
from BLL.movies_bl import MoviesBL

movies_bl = MoviesBL()
movies = Blueprint("movies", __name__)

# GET All


@movies.route('/', methods=['GET'])
def get_all_movies():
    movies = movies_bl.get_all_movies()
    return jsonify(movies)

# GET by ID


@movies.route('/<id>', methods=['GET'])
def get_movie(id):
    movie = movies_bl.get_movie(id)
    return jsonify(movie)

# POST


@movies.route('/', methods=['POST'])
def add_movie():
    name = request.json["name"]
    genres = request.json["genres"]
    image = request.json["image"]
    premiered = request.json["premiered"]
    if len(name) > 0 and len(genres) > 0 and len(image) > 0 and len(premiered) > 0:
        obj = {"name": name, "genres": genres,
               "image": image, "premiered": premiered}
        movie = movies_bl.add_movie(obj)
        return jsonify(movie)
    else:
        return "All Fields Are Required"

# PUT


@movies.route('/<id>', methods=['PUT'])
def update_movie(id):
    obj = request.json
    movie = movies_bl.update_movie(id, obj)
    return jsonify(movie)

# DELETE


@movies.route('/<id>', methods=['DELETE'])
def delete_movie(id):
    movie = movies_bl.delete_movie(id)
    return jsonify(movie)
