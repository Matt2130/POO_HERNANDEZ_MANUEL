menu = {
"Abstracción" : 1,
"Encapsulamiento" : 2,
"Herencia" : 3,
"Polimorfismo" : 4,
"Salir" : 5 
}

def abstraccion():
    print("""En POO, la abstracción permite enfocarse en los aspectos esenciales de un objeto, 
ocultando los detalles innecesarios.""")
    
def encapsulamiento():
    print("""El encapsulamiento es el proceso de agrupar datos y métodos que operan sobre esos
datos dentro de una misma unidad, generalmente una clase.""")
    
def herencia():
    print("""La herencia es un mecanismo que permite crear nuevas clases basadas en clases existentes.
Una clase derivada (o subclase) hereda atributos y métodos de una clase base (o superclase),
lo que facilita la reutilización del código.""")

def polimorfismo():
    print("""El polimorfismo es la capacidad de un objeto de tomar diferentes formas. 
En POO, esto significa que una referencia a una clase base puede apuntar a objetos de sus subclases
y que estos objetos pueden responder de manera diferente a la misma llamada de método.""")
        
for i,j in menu.items():
    print(f"{i} : {j}")
    
while True:
    x = input("Ingrese un número ")

    if x == "1":
        print("Definición de abstracción")
        abstraccion()
        print("\n")
        
    elif x == "2":
        print("Definición de encapsulamiento")
        encapsulamiento()
        print("\n")
        
    elif x == "3":
        print("Definición de herencia")
        herencia()
        print("\n")
        
    elif x == "4":
        print("Definición de polimorfismo")
        polimorfismo()
        print("\n")
        
    elif x == "5":
        print("Saliendo")
        break

    else:
        print("Ingrese otro número")