from app import mysql

def get_editorials():
    cursor = mysql.connection.cursor()

    cursor.execute("select * from editoriales")

    cols = [col[0] for col in cursor.description]

    editorials = [dict(zip(cols, row)) for row in cursor.fetchall()]

    cursor.close()

    return editorials


def get_editorial(id):

    cursor = mysql.connection.cursor()

    cursor.execute("select * from editoriales where id = %s",(id,))

    cols = [col[0] for col in cursor.description]

    
    response = dict(zip(cols, cursor.fetchone()))

    cursor.close()

    if response:
        return response
    else:
        return {"Mensaje": "No hay"}
    
 
def create_editorial(data):
    nombre = data.get("nombre")

    cursor = mysql.connection.cursor()

    cursor.execute("insert into editoriales (nombre) values (%s)", (nombre,))

    mysql.connection.commit()
    cursor.close()

    return {"Mensaje":"Editorial agregado"}

def update_editorial(id,data):
    if not data:
        return {"Mensaje":"Debe enviarle los datos"}
    update_query = "update editoriales set "
    update_data = []

    cursor = mysql.connection.cursor()


    for field, value in data.items():
        if field in ["nombre",]:
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

def delete_editorial(id):
    cursor = mysql.connection.cursor()

    cursor.execute("delete from editoriales where id = %s", (id,))
    mysql.connection.commit()

    cursor.close()

    return {"Mensaje":"Editorial eliminado con exito"}