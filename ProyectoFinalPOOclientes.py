from ProyectoFinalPOOConexion import * #llamar el archivo,para poder usar las funciones 

class Clientes: #mi clase cliente hereda todos los atributos y métodos de mi clase principal 'Conexion'
    
    def mostrarClientes(): # **** este vendría siendo mi boton de consultar ****
        try:
            
            cone = Conexion.ConexionBaseDatos()
            cursor = cone.cursor() #ayuda a las consltas hacia la BD
            cursor.execute("SELECT * FROM clientes;")#ejecuta la query para ver los datos        
            miResiultado = cursor.fetchall() #resultado de todo el conjunto pedido
            cone.commit()
            cone.close()
            return miResiultado
            
        except mysql.connector.Error as error:
            print("Error de mostrar datos {}".format(error))
          
    def ingresoDeClientes(nombres,dirección,télefono,tipoDeCompra):
        try:
            
            cone = Conexion.ConexionBaseDatos()
            cursor = cone.cursor() #ayuda a las consltas hacia la BD
            sql = "INSERT INTO clientes VALUES(null,%s,%s,%s,%s);"
            #la variable valores tiene que ser una tupla
            #como mínima expresión es: (valor,) la coma hace que sea una tupla
            #entonces las tuplas son listas inmutables, no se modifican
            
            valores = (nombres,dirección,télefono,tipoDeCompra)
            cursor.execute(sql,valores) #cursor ejecutará la union de sql con sus respectivos valores
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error de ingreso a la base de datos {}".format(error))
            
    def modificarClientes(n_clientes,nombres,dirección,télefono,tipoDeCompra):
        try:
            
            cone = Conexion.ConexionBaseDatos()
            cursor = cone.cursor() #ayuda a las consltas hacia la BD
            sql = "UPDATE clientes SET clientes.nombres = %s,clientes.dirección = %s,clientes.télefono = %s,clientes.tipoDeCompra = %s WHERE clientes.n°_clientes = %s;"
            valores = (nombres,dirección,télefono,tipoDeCompra,n_clientes)
            cursor.execute(sql,valores) #cursor ejecutará la union de sql con sus respectivos valores
            cone.commit()
            print(cursor.rowcount,"Registro ingresado")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error de actualizaciónde datos {}".format(error))
            
    def eliminarClientes(n_clientes):
        try:
            
            cone = Conexion.ConexionBaseDatos()
            cursor = cone.cursor() #ayuda a las consltas hacia la BD
            sql = "DELETE FROM clientes WHERE clientes.n°_clientes = %s;" #indica un parametro (%s)
            valores = (n_clientes,)
            cursor.execute(sql,valores) #cursor ejecutará la union de sql con sus respectivos valores
            cone.commit()
            print(cursor.rowcount,"Registro eliminado")
            cone.close()
            
        except mysql.connector.Error as error:
            print("Error de eliminación de datos {}".format(error))