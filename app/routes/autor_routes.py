
from flask import Blueprint, jsonify, request

# Vamos a importar los controladores
from app.controllers.autor_controller import get_autors, get_autor, create_autor, update_autor, delete_autor

autor = Blueprint('autor', __name__)

@autor.route("/autor", methods=["GET"])
def get_all_autors():
    return jsonify(get_autors())

@autor.route("/autors/<autor_id>", methods=["GET"])
def get_one_autor(autor_id):
    return jsonify(get_autor(autor_id))
@autor.route("/autors", methods=["POST"])
def add_autor():
    return jsonify(create_autor(request.json))


@autor.route("/autors/<autor_id>", methods=["PATCH"])
def update_autor_id(autor_id):
    return jsonify(update_autor(autor_id, request.json))

@autor.route("/autors/<autor_id>", methods=["DELETE"])
def eliminate_autor(autor_id):
    return jsonify(delete_autor(autor_id))