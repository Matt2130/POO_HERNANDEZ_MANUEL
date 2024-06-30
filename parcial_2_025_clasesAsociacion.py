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
            print(f"{i.nombreDelLibro}")

class Autor: #Clase tipo agregación
    def __init__(self, nombre, fechaNacimiento, edad):
        self.nombre = nombre #atributo
        self.fechaNacimiento = fechaNacimiento #atributo
        self.edad = edad #atributo

    def nacimiento(self): #Métodos
        print(f"\nEl autor {self.nombre} nació en {self.fechaNacimiento}")

    def publicar(libro): #Métodos
        print(f"El autor {libro.autor} ha publicado el libro {libro.nombreDelLibro}")
    
    def citar(self): #Métodos
        print(f"{self.nombre} ha citado a otro autor a la edad de {self.edad}")
 
#Objetos de mi clase Libro
libro1 = Libro("Miguel de Cervantes", "Don Quijote de la mancha", 1605)
libro2 = Libro("Gabriel García Marquez","Cien años de soledad",1967)
libro3 = Libro("Patrick Rothfuss","El nombre del viento",2007)

#Uso de los métodos de mi clase Libro (clase principal) 
libro1.leer()
libro2.rentar()
libro3.noExistente()
print("")

#Objeto
estante = Estante("manuel")

#Método
estante.ponerLibros(libro1)
estante.ponerLibros(libro2)
estante.ponerLibros(libro3)

estante.buscarSeccion()

#Objetos de mi clase Autor
info_autor1 = Autor("Miguel de Cervantes", "29/09/1547",69) 
info_autor2 = Autor("Gabriel García Marquez", "06/03/1927", 87) 
info_autor3 = Autor("Patrick Rothfuss", "06/06/1973",51)

autor = Autor
autor.nacimiento(info_autor3)
autor.publicar(libro1)
autor.citar(info_autor2)