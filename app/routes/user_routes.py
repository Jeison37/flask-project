from flask import Blueprint, jsonify, request

from app.controllers.user_controller import create_user, delete_user, get_user, get_users, update_user

user = Blueprint("user", __name__)

@user.route("/users", methods=["GET"])
def get_all_users():
    return jsonify(get_users())

@user.route("/users/<user_id>", methods=["GET"])
def get_one_user(user_id):
    return jsonify(get_user(user_id))

@user.route("/users", methods=["POST"])
def add_user():
    return jsonify(create_user(request.json))

@user.route("/users/<user_id>", methods=["PATCH"])
def update_user_id(user_id):
    return jsonify(update_user(user_id, request.json))

@user.route("/users/<user_id>", methods=["DELETE"])
def eliminate_user(user_id):
    return jsonify(delete_user(user_id))