class Libro:
    def __init__(self, autor, nombreDelLibro, edicion):
        self.autor = autor #Atributos
        self.nombreDelLibro = nombreDelLibro #Atributos
        self.edicion = edicion #Atributos
    
    def leer(self): #Métodos
        print("Leido")
        
    def rentar(self): #Métodos
        print("Rentado")
        
    def noExistente(self): #Métodos
        print("El libro no se encuentra aquí")
        
libro1 = Libro("Leo", "Azul el mar", 5) #Objetos
libro2 = Libro("Felipe","El hoy",3) #Objetos

print("Para el Libro 1 están los siguientes datos:")
print(f"""Autor : {libro1.autor}
Nombre del libro : {libro1.nombreDelLibro}
Edición : {libro1.edicion}\n""")

print("Para el Libro 2 están los siguientes datos:")
print(f"""Autor : {libro2.autor}
Nombre del libro : {libro2.nombreDelLibro}
Edición : {libro2.edicion}\n""")

libro1.leer()
libro2.rentar()
libro1.noExistente()