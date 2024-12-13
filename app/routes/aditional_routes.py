from flask import Blueprint, jsonify, request

from app.controllers.aditional_controller import get_info

aditional = Blueprint("aditional",__name__)

@aditional.route("/aditional", methods=["GET"])
def aditional_response():
    return jsonify(get_info())