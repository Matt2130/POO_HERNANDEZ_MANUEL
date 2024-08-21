import mysql.connector #conexión con la BD

class Conexion:
    def ConexionBaseDatos():
        try:
            conexion = mysql.connector.connect(user='root',
                                               password='',
                                               host='127.0.0.1',
                                               database='tienda_blancos',
                                               port='3306')
            
            print("Conexión correcta")
            
            return conexion #return para verificar si la conexion con la BD es correcta
        
        except mysql.connector.Error as error:
            print("Error al conectarte a la base de datos {}".format(error)) #en caso de error regresara este mensaje
            
    ConexionBaseDatos() #llamar a la función para poder establecer la conexión