from flask import Blueprint, jsonify, request

from app.controllers.book_controller import create_book, delete_book, get_book, get_books, update_book

book = Blueprint("book", __name__)

@book.route("/books", methods=["GET"])
def get_all_books():
    return jsonify(get_books())

@book.route("/books/<book_id>", methods=["GET"])
def get_one_book(book_id):
    return jsonify(get_book(book_id))

@book.route("/books", methods=["POST"])
def add_book():
    return jsonify(create_book(request.json))

@book.route("/books/<book_id>", methods=["PATCH"])
def update_book_id(book_id):
    return jsonify(update_book(book_id, request.json))

@book.route("/books/<book_id>", methods=["DELETE"])
def eliminate_book(book_id):
    return jsonify(delete_book(book_id))