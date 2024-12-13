from app import mysql

def get_info():
    cursor = mysql.connection.cursor()

    cursor.execute("select libros.id as libro_id, libros.titulo, autores.nombre as autor_del_libro, generos.nombre as genero, reviews.contenido as contenido_de_la_reseña, usuarios.nombre as usuario_que_realizo_la_reseña from libros inner join autores on libros.autor_id = autores.id inner join generos on libros.genero_id = generos.id inner join reviews on reviews.libro_id = libros.id inner join usuarios on usuarios.id = reviews.usuario_id")

    cols = [col[0] for col in cursor.description]

    aditional = [dict(zip(cols, row)) for row in cursor.fetchall()]

    cursor.close()

    return aditional