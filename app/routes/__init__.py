from .autor_routes import autor
from .aditional_routes import aditional
from .book_routes import book
from .genre_routes import genre
from .user_routes import user
def register_routes(app):
    app.register_blueprint(autor)
    app.register_blueprint(aditional)
    app.register_blueprint(book)
    app.register_blueprint(genre)
    app.register_blueprint(user)