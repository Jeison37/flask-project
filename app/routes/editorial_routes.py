from flask import Blueprint, jsonify, request

from app.controllers.editorial_controller import create_editorial, delete_editorial, get_editorial, get_editorials, update_editorial

editorial = Blueprint("editorial", __name__)

@editorial.route("/editorials", methods=["GET"])
def get_all_editorials():
    return jsonify(get_editorials())

@editorial.route("/editorials/<editorial_id>", methods=["GET"])
def get_one_editorial(editorial_id):
    return jsonify(get_editorial(editorial_id))

@editorial.route("/editorials", methods=["POST"])
def add_editorial():
    return jsonify(create_editorial(request.json))

@editorial.route("/editorials/<editorial_id>", methods=["PATCH"])
def update_editorial_id(editorial_id):
    return jsonify(update_editorial(editorial_id, request.json))

@editorial.route("/editorials/<editorial_id>", methods=["DELETE"])
def eliminate_editorial(editorial_id):
    return jsonify(delete_editorial(editorial_id))