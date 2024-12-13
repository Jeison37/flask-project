from app import mysql

def get_reviews():
    cursor = mysql.connection.cursor()

    cursor.execute("select * from reviews")

    cols = [col[0] for col in cursor.description]

    reviews = [dict(zip(cols, row)) for row in cursor.fetchall()]

    cursor.close()

    return reviews


def get_review(id):

    cursor = mysql.connection.cursor()

    cursor.execute("select * from reviews where id = %s",(id,))

    cols = [col[0] for col in cursor.description]

    
    response = dict(zip(cols, cursor.fetchone()))

    cursor.close()

    if response:
        return response
    else:
        return {"Mensaje": "No hay"}
    
 
def create_review(data):
    contenido = data.get("contenido")
    libro_id = data.get("libro_id")
    usuario_id = data.get("usuario_id")
    

    cursor = mysql.connection.cursor()

    cursor.execute("insert into reviews (contenido,libro_id,usuario_id) values (%s)", (contenido,libro_id,usuario_id))

    mysql.connection.commit()
    cursor.close()

    return {"Mensaje":"Reseña agregada"}

def update_review(id,data):
    if not data:
        return {"Mensaje":"Debe enviarle los datos"}
    update_query = "update reviews set "
    update_data = []

    cursor = mysql.connection.cursor()


    for field, value in data.items():
        if field in ["contenido","libro_id","usuario_id"]:
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

def delete_review(id):
    cursor = mysql.connection.cursor()

    cursor.execute("delete from reviews where id = %s", (id,))
    mysql.connection.commit()

    cursor.close()

    return {"Mensaje":"Reseña eliminada con exito"}