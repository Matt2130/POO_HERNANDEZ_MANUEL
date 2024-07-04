menu = {
    1 : "Clase Principal 'LIBRO'",
    2 : "Clase tipo Asociación 'ESTANTE'",
    3 : "Clase tipo Agregación 'AUTOR'",
    4 : "Clase tipo Composición 'CONTENIDO DEL LIBRO'",
    5 : "Clase tipo Herencia 'LIBRO PRESTADO",
    6 : "Clase tipo Dependencia 'CARACTERÍSTICAS",
    7 : "Clase tipo Asociación 'LECTOR",
    8 : "Clase tipo Agregación 'CREDENCIAL'",
    9 : "Salir del programa"
}

class Libro: #clase principal
    def __init__(self, autor, nombreDelLibro, añoDePublicacion): #init es el constructor
        self.autor = autor  #Atributos
        self.nombreDelLibro = nombreDelLibro #Atributos
        self.añoDePublicacion = añoDePublicacion #Atributos

    def leer(self): #Métodos
        print(f"El libro {self.nombreDelLibro} está siendo Leido")

    def rentar(self): #Métodos
        print(f"{self.autor} ha rentado un libro")

    def noExistente(self): #Métodos
        print(f"El libro '{self.nombreDelLibro}' no se encuentra aquí desde el año {self.añoDePublicacion}")

    def componentes(self, compuesto): #Método dependiente de la clase compuesto (relación debil)
        print(f"{self.nombreDelLibro} esta compuesto de varios objetos. Como : {compuesto.tamaño_libro}, {compuesto.cantidad_paginas} y {compuesto.material}")

class Estante: #Clase tipo asociación
    def __init__(self, nombreDelLibro):
        self.nombreDelLibro = nombreDelLibro #atributos
        self.libros = [] #atributos

    def ponerLibros(self, libro): #Métodos
        self.libros.append(libro)
        print(f"{libro.nombreDelLibro} se ha puesto en el estante")

    def buscarSeccion(self): #Métodos
        print(f"\nEn esté estante estan los siguientes libros:")
        for i in self.libros:
            print(f"{i.nombreDelLibro}") #uso de un ciclo for

class Autor: #Clase tipo agregación
    def __init__(self, nombre, fechaNacimiento, edad):
        self.nombre = nombre #atributo
        self.fechaNacimiento = fechaNacimiento #atributo
        self.edad = edad #atributo

    def nacimiento(self): #Métodos
        print(f"El autor {self.nombre} nació en {self.fechaNacimiento}")

    def publicar(libro): #Métodos
        print(f"El autor {libro.autor} ha publicado el libro {libro.nombreDelLibro}")

    def citar(self): #Métodos
        print(f"{self.nombre} ha citado a otro autor a la edad de {self.edad}")

class ContenidoDelLibro(Libro): #clase composición
    def __init__(self, genero, tipografia, clasificacionDelLibro):
        self.genero = genero #atributo
        self.tipografia = tipografia #atributo
        self.clasificacionDelLibro = clasificacionDelLibro

    def clasificacion(libro, self): #Método
        print(f"El tipo de genero del libro {libro.nombreDelLibro} es {self.genero}")

    def estiloDeTexto(libro, self): #Método
        print(f"El estilo de texto en el libro {libro.nombreDelLibro} es {self.tipografia}")

    def descripcion(self, libro): #Método
        if self.clasificacionDelLibro:
            print(f"El libro {libro.nombreDelLibro} es una Novela")
        else:
            print(f"El libro {libro.nombreDelLibro} no es una Novela")

class LibroPrestado(Libro): #clase de tipo herencia
    def __init__(self, autor, nombreDelLibro, añoDePublicacion, libroEnExistencia):
        super().__init__(autor, nombreDelLibro, añoDePublicacion) #atributo de mi clase princial Libro
        self.libroEnExistencia = libroEnExistencia #atributo nuevo para la clase

    def renta(self): #método
        if self.libroEnExistencia:
            print(f"El libro {self.nombreDelLibro} si está disponible para su renta")
        else:
            print(f"El libro {self.nombreDelLibro} no está disponible para su renta")
        
class Caracteristicas(): #clase tipo dependencia 
    def __init__(self, tamaño_libro, cantidad_paginas, material):
        self.tamaño_libro = tamaño_libro
        self.cantidad_paginas = cantidad_paginas
        self.material = material

    def compuesto(libro, self):
        print(f"""El libro {libro.nombreDelLibro} tiene las siguientes características:
            Mide {self.tamaño_libro}, tiene {self.cantidad_paginas} páginas y esta hecho de {self.material}.""")
    

class Lector: #asociacion
    def __init__(self, nombre, librosLeidos, edad):
        self.nombre = nombre #atributos
        self.librosLeidos = librosLeidos #atributos
        self.edad = edad #atributos
        
    def lectura(self): #Métodos
        print(f"El lector {self.nombre} ha leído {self.librosLeidos} libros")
        
    def acceso_todoElCatalogo(self): #Métodos
        if self.edad:
            print(f"El lector {self.nombre} tiene la edad para leer los libros con clasificación + 18")
        else:
            print(f"El lector {self.nombre} no tiene la edad para leer los libros con clasificación + 18")
        
class Credencial: #agregación
    def __init__(self):
        self.nombreDeUsuario = [] #atributos
        self.carrera = [] #atributos
        self.ID = [] #atributos
                
    def registro(self): #Métodos
        usuario = input("Ingrese su nombre de usuario: ")
        self.nombreDeUsuario.append(usuario)
        
        carrera = input("Ingrese su carrera: ")
        self.carrera.append(carrera)
        
        ID = input("Ingrese la matrícula que se le dio: ")
        self.ID.append(ID)
        
        print(f"Su registro se ha realizado con exitó. Ya puede rentar libros.")

    def prestamo(self): #Métodos
        ID = input(f"Ingrese la matrícula de {self.nombreDeUsuario[0]}: ")
        while ID != "class":
            ID = input("Matrícula incorreta. Por favor ingrese una matrícula correcta: ")
        
        print(f"{self.nombreDeUsuario[0]} de la carrera {self.carrera[0]} sí pertenece a esta escuela")

def clear_screen():
    print("\033c", end="")        

while True:
    print(f"""MENÚ DE LA CLASE LIBRO:
    Escoga una opción a ejecutar\n""")
    for i,j in menu.items():
        print(f"{i}) {j}")
    opciones = input("\nIngrese la opción que desea ejecutar del código: ")
    
    if opciones == "1":
        clear_screen()
        print(f"--------Clase Principal 'LIBRO'--------\n")
        libro1 = Libro("Miguel de Cervantes", "Don Quijote de la mancha", 1605)
        libro2 = Libro("Gabriel García Marquez","Cien años de soledad",1967)
        libro3 = Libro("Patrick Rothfuss","El nombre del viento",2007)
        #Uso de los métodos de mi clase Libro (clase principal) 
        libro1.leer()
        libro2.rentar()
        libro3.noExistente()
        print("")
        
    elif opciones == "2":
        clear_screen()
        print(f"--------Clase tipo Asociación 'ESTANTE'--------\n")
        estante = Estante("")
        estante.ponerLibros(libro1) #Método
        estante.ponerLibros(libro2) #Método
        estante.ponerLibros(libro3) #Método
        estante.buscarSeccion() #Método uso del ciclo for para imprimir los nombres de los libros
        print("")
    
    elif opciones == "3":
        clear_screen()
        print(f"--------Clase tipo Agregación 'AUTOR'--------\n")
        info_autor1 = Autor("Miguel de Cervantes", "29/09/1547",69) 
        info_autor2 = Autor("Gabriel García Marquez", "06/03/1927", 87) 
        info_autor3 = Autor("Patrick Rothfuss", "06/06/1973",51)
        autor = Autor #Creación de una variable para el uso de sus métodos
        info_autor3.nacimiento() #Método
        autor.publicar(libro1) #Método
        info_autor2.citar() #Método
        print("")
        
    elif opciones == "4":
        clear_screen()
        print(f"--------Clase tipo Composición 'CONTENIDO DEL LIBRO'--------\n")
        libro1 = Libro("Miguel de Cervantes", "Don Quijote de la mancha", 1605)
        libro2 = Libro("Gabriel García Marquez","Cien años de soledad",1967)
        libro3 = Libro("Patrick Rothfuss","El nombre del viento",2007)
        ContenidoDelLibro1 = ContenidoDelLibro("Novela", "Polifónica", True)
        ContenidoDelLibro2 = ContenidoDelLibro("Realismo magico","Abstracca", False)
        ContenidoDelLibro3 = ContenidoDelLibro("Alta fantasia", "New roman", False)
        #Uso de los métodos de mi clase ContenidoDelLibro
        contenido = ContenidoDelLibro # creación de una variable para para el uso de los métodos
        contenido.clasificacion(libro1, ContenidoDelLibro1)
        contenido.estiloDeTexto(libro2, ContenidoDelLibro2)
        ContenidoDelLibro3.descripcion(libro3)
        print("")
        
    elif opciones == "5":
        clear_screen()
        print(f"--------Clase tipo Herencia 'LIBRO PRESTADO'--------\n")
        datosDelLibroPrestado1 = LibroPrestado("Miguel de Cervantes", "Don Quijote de la mancha", 1605, True)
        datosDelLibroPrestado2 = LibroPrestado("Gabriel García Marquez","Cien años de soledad",1967, True)
        datosDelLibroPrestado3 = LibroPrestado("Patrick Rothfuss","El nombre del viento",2007, False)
        #Uso de los métodos de mi clase ContenidoDelLibro
        libroprestado = LibroPrestado # creación de una variable para para el uso de los métodos
        libroprestado.renta(datosDelLibroPrestado1)
        libroprestado.renta(datosDelLibroPrestado2)
        libroprestado.renta(datosDelLibroPrestado3)
        print("")
        
    elif opciones == "6":
        clear_screen()
        print(f"--------Clase tipo Dependencia 'CARACTERÍSTICAS'--------\n")
        carac1 = Caracteristicas("50 cm", 268, "Cuero")
        carac2 = Caracteristicas("45 cm", 562, "Papel")
        carac3 = Caracteristicas("55 cm", 300, "Lienzo")
        #Uso de los métodos de mi clase Características
        caracter = Caracteristicas # creación de una variable para para el uso de los métodos
        caracter.compuesto(libro1, carac1)
        caracter.compuesto(libro2, carac2)
        caracter.compuesto(libro3, carac3)
        print("")
        #Uso de mi método de relación debil en mi clase dependencia
        print("Uso del método de la clase dependencia")
        libro2.componentes(carac3)
        libro3.componentes(carac1)
        libro1.componentes(carac2)
        print("")
        
    elif opciones == "7":
        clear_screen()
        print(f"--------Clase tipo Asociación 'LECTOR'--------\n")
        lector1 = Lector("Leo", 5, True)
        lector2 = Lector("Manuel", 9, False)
        lector3 = Lector("Juan", 4, True)
        #Métodos de la clase
        lector1.lectura()
        lector2.lectura()
        lector2.acceso_todoElCatalogo()
        lector3.acceso_todoElCatalogo()
        print("")
        
    elif opciones == "8":
        clear_screen()
        print(f"--------Clase tipo Agregación 'CREDENCIAL PARA PEDIR PRESTAMOS DE LIBROS'--------\n")
        print("Solicitud de ID, para rentar libros")
        estudiante1 = Credencial()
        estudiante2 = Credencial()
        #Método de la clase
        print("Registro del Estudiante 1")
        estudiante1.registro()
        print("")
        print("Registro del Estudiante 2")
        estudiante2.registro()
        print("")
        print("Verificación del Estudiante 1")
        estudiante1.prestamo()
        print("")
        print("Verificación del Estudiante 2")
        estudiante2.prestamo()
        print("")
        
    elif opciones == "9":
        print("Saliendo.....")
        break
        
    else:
        clear_screen()
        print(f"\n--------Opción invalida. Ponga un número validó--------\n")