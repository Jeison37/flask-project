from app import mysql


def get_users():

    cursor = mysql.connection.cursor()
    
    cursor.execute("select * from usuarios")

    [print(col) for col in cursor.description]

    cols = [col[0] for col in cursor.description]

    
    users = [dict(zip(cols, row)) for row in cursor.fetchall()]

    cursor.close()


    return users

def get_user(id):

    cursor = mysql.connection.cursor()

    cursor.execute("select * from usuarios where id = %s",(id,))

    cols = [col[0] for col in cursor.description]

    
    response = dict(zip(cols, cursor.fetchone()))

    cursor.close()

    if response:
        return response
    else:
        return {"Mensaje": "No hay"}
    
 
def create_user(data):
    nombre = data.get("nombre")
    

    cursor = mysql.connection.cursor()

    cursor.execute("insert into usuarios (nombre) values (%s)", (nombre,))

    mysql.connection.commit()
    cursor.close()

    return {"Mensaje":"Usuario agregado"}

def update_user(id,data):
    if not data:
        return {"Mensaje":"Debe enviarle los datos"}
    update_query = "update usuarios set "
    update_data = []

    cursor = mysql.connection.cursor()


    for field, value in data.items():
        if field in ["nombre",]:
            update_query += f"{field} = %s, "
            update_data.append(value)

    if not update_data:
        return {"Mensaje": "Debe enviarse los datos"}
    
    update_query = update_query.rstrip(", ")


    update_query += " where id = %s"

    update_data.append(id)

    cursor.execute(update_query, tuple(update_data,))
    mysql.connection.commit()
    cursor.close()

    return {"Mensaje": "Actualizado"}

def delete_user(id):
    cursor = mysql.connection.cursor()

    cursor.execute("delete from usuarios where id = %s", (id,))
    mysql.connection.commit()

    cursor.close()

    return {"Mensaje":"Usuario eliminado con exito"}
