import mysql.connector
from mysql.connector import Error

# Función para conectar a la base de datos
conexion = mysql.connector.connect(
        host='localhost', #host de mi base de datos
        user='root', #usuario
        password='', #contraseña
        database='animales' #nombre de mi base de datos
)

# Interacción con la base de datos a tráves del objeto cursor
cursor = conexion.cursor()

# Consulta SHOW para mostrar un registro
def show():
    cursor.execute("SELECT * FROM leones")
    result = cursor.fetchall()
    for row in result:
        print(row)

# Consulta INSERT para añadir un nuevo registro
def insert():
    query = "INSERT INTO leones (identificador, raza, edad, ubicacion) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, ("", "africano", "5", "kenia"))
    conexion.commit()
    print("Leon insertado exitosamente")

# Consulta DELETE para eliminar un registro
def delete():
    show()
    identificador = input("ingresar el identificador a delete: ")
    query = "DELETE FROM leones WHERE identificador = %s"
    tupla = cursor.execute(query, (identificador))
    lista = list(tupla)
    conexion.commit()
    print("Leon eliminado exitosamente")

# Consulta UPDATE para actualizar un registro
def update():
    show()
    identificador = input("ingresar el identificador a modificar: ")
    query = "UPDATE leones SET identificador = %s, raza = %s, edad = %s, ubicacion = %s WHERE identificador = %s"
    cursor.execute(query, ("", "leon de la india", "3", "america"))
    conexion.commit()
    print("Leon actualizado exitosamente")

print("Los datos ingresados se han agregado en la base de datos")
insert()
print("")

print("Mostrar datos")
show()
print("")

print("Datos eliminados")
delete()
print("")

print("Datos actualizados")
update()
print("")

if conexion.is_connected():
    conexion.close()
    print("Conexión cerrada")