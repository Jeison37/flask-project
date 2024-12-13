from app import mysql

def get_books():
    cursor = mysql.connection.cursor()

    cursor.execute("select * from libros")

    cols = [col[0] for col in cursor.description]

    books = [dict(zip(cols, row)) for row in cursor.fetchall()]

    cursor.close()

    return books


def get_book(id):

    cursor = mysql.connection.cursor()

    cursor.execute("select * from libros where id = %s",(id,))

    cols = [col[0] for col in cursor.description]

    
    response = dict(zip(cols, cursor.fetchone()))

    cursor.close()

    if response:
        return response
    else:
        return {"Mensaje": "No hay"}
    
 
def create_book(data):
    titulo = data.get("titulo")
    ano_publicacion = data.get("ano_publicacion")
    autor_id = data.get("autor_id")
    genero_id = data.get("genero_id")
    editorial_id = data.get("editorial_id")
    

    cursor = mysql.connection.cursor()

    cursor.execute("insert into libros (titulo,ano_publicacion,autor_id,genero_id,editorial_id) values (%s,%s,%s,%s,%s)", (titulo,ano_publicacion,autor_id,genero_id,editorial_id))

    mysql.connection.commit()
    cursor.close()

    return {"Mensaje":"Libro agregado"}

def update_book(id,data):
    if not data:
        return {"Mensaje":"Debe enviarle los datos"}
    update_query = "update libros set "
    update_data = []

    cursor = mysql.connection.cursor()


    for field, value in data.items():
        if field in ["titulo","ano_publicacion","autor_id","genero_id","editorial_id"]:
            update_query += f"{field} = %s, "
            update_data.append(value)

    if not update_data:
        return {"Mensaje": "Debe enviase los datos"}
    
    update_query = update_query.rstrip(", ")


    update_query += " where id = %s"

    update_data.append(id)

    cursor.execute(update_query, tuple(update_data,))
    mysql.connection.commit()
    cursor.close()

    return {"Mensaje": "Actualizado"}

def delete_book(id):
    cursor = mysql.connection.cursor()

    cursor.execute("delete from libros where id = %s", (id,))
    mysql.connection.commit()

    cursor.close()

    return {"Mensaje":"Libro eliminado con exito"}