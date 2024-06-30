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

 
#Objetos de mi clase principal Libro
print(f"    ****************Clase principal****************")
libro1 = Libro("Miguel de Cervantes", "Don Quijote de la mancha", 1605)
libro2 = Libro("Gabriel García Marquez","Cien años de soledad",1967)
libro3 = Libro("Patrick Rothfuss","El nombre del viento",2007)
#Uso de los métodos de mi clase Libro (clase principal) 
libro1.leer()
libro2.rentar()
libro3.noExistente()
print("")

#Objeto de mi clase Estante (asociación)
print(f"    ****************Clase Estante****************")
estante = Estante("")
estante.ponerLibros(libro1) #Método
estante.ponerLibros(libro2) #Método
estante.ponerLibros(libro3) #Método
estante.buscarSeccion() #Método uso del ciclo for para imprimir los nombres de los libros
print("")

#Objetos de mi clase Autor (agregación)
print(f"    ****************Clase Autor****************")
info_autor1 = Autor("Miguel de Cervantes", "29/09/1547",69) 
info_autor2 = Autor("Gabriel García Marquez", "06/03/1927", 87) 
info_autor3 = Autor("Patrick Rothfuss", "06/06/1973",51)
autor = Autor #Creación de una variable para el uso de sus métodos
info_autor3.nacimiento() #Método
autor.publicar(libro1) #Método
info_autor2.citar() #Método
print("")

#Objetos de mi clase contenidodellibro (composición)
print(f"    ****************Clase ContenidoDelLibro****************")
ContenidoDelLibro1 = ContenidoDelLibro("Novela", "Polifónica", True)
ContenidoDelLibro2 = ContenidoDelLibro("Realismo magico","Abstracca", False)
ContenidoDelLibro3 = ContenidoDelLibro("Alta fantasia", "New roman", False)
#Uso de los métodos de mi clase ContenidoDelLibro
contenido = ContenidoDelLibro # creación de una variable para para el uso de los métodos
contenido.clasificacion(libro1, ContenidoDelLibro1)
contenido.estiloDeTexto(libro2, ContenidoDelLibro2)
ContenidoDelLibro3.descripcion(libro3)