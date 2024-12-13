from flask import Blueprint, jsonify, request

from app.controllers.genre_controller import create_genre, delete_genre, get_genre, get_genres, update_genre

genre = Blueprint("genre", __name__)

@genre.route("/genres", methods=["GET"])
def get_all_genres():
    return jsonify(get_genres())

@genre.route("/genres/<genre_id>", methods=["GET"])
def get_one_genre(genre_id):
    return jsonify(get_genre(genre_id))

@genre.route("/genres", methods=["POST"])
def add_genre():
    return jsonify(create_genre(request.json))

@genre.route("/genres/<genre_id>", methods=["PATCH"])
def update_genre_id(genre_id):
    return jsonify(update_genre(genre_id, request.json))

@genre.route("/genres/<genre_id>", methods=["DELETE"])
def eliminate_genre(genre_id):
    return jsonify(delete_genre(genre_id))