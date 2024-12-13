from app import mysql

def get_autors():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from autores")

    cols = [col[0] for col in cursor.description]

    autors = [dict(zip(cols,row)) for row in cursor.fetchall()]

    cursor.close()

    return autors

def get_autor(id):
    cursor = mysql.connection.cursor()
    cursor.execute("select * from autores where id = %s", (id,))

    cols = [col[0] for col in cursor.description]

    res = dict(zip(cols, cursor.fetchone()))

    cursor.close()

    if res:
        return res
    else:
        return {"Mensaje": "No hay"}
    
def create_autor(data):
    nombre = data.get("nombre")
    cursor = mysql.connection.cursor()
    cursor.execute("insert into autores (nombre) values (%s)", (nombre,))
    mysql.connection.commit()
    cursor.close()

    return {"Mensaje":"Autor agregado"}

def update_autor(id,data):
    if not data:
        return {"Mensaje":"Debe enviarse los datos"}
    
    update_query = "update autores set "
    update_data = []

    cursor = mysql.connection.cursor()

    for field, value in data.items():
        if field in ["nombre"]:
            update_query += f"{field} = %s, "
            update_data.append(value)

    if not update_data:
        return {"Mensaje":"Debe enviarse los datos"}
    
    update_query += " where id = %s"

    update_data.append(id)
    cursor.execute(update_query,tuple(update_data,))
    mysql.connection.commit()
    cursor.close()
    return {"Mensaje": "Actualizado"}

def delete_autor(id):
    cursor = mysql.connection.commit()

    cursor.execute("delete from auteres where id = %s", (id,))
    mysql.connection.commit()

    cursor.close()

    return {"Mensaje":"Autor eliminado con exito"}