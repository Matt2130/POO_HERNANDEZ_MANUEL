#TUPLAS
#¿Qué son? 
#Son un tipo de estructura de datos que permite almacenar una secuencia
#de elmentos inmutables. Esto quiere decir que no pueden cambiar, agregar
#o eliminar.

#CARACTERISTICAS
#no se modifica
#tiene orden definidoy se acceden mediante indices
#puede tener elementos duplicados
#pueden tener diferentes tipos de datos

#ACCIONES COMUNES
#CREACION - Utilizando parentesis 
tupla1 = (0,52,"hola","aquellos",True)
tupla2 = (8,96,"café",False,2)
print("Creación de las tuplas")
print(tupla1)
print(f"{tupla2}\n")

#ACCESO A ELEMENTOS - UTILIZAR []
print("Acceder a los elemntos de la tupla")
print(f"{tupla1[2]}\n")

#CONCATENACIÓN DE LA TUPLA - UTILIZANDO OPERADOR + 
print("Concatenación de la tupla")
tupla_concatenada = tupla1 + tupla2
print(f"{tupla_concatenada}\n")

#REPETICION DE TUPLAS - UTILIZAR OPERADOR * 
tupla_repetida = tupla2 * 2
print("Repetir la tupla")
print(f"{tupla_repetida}\n")

#DESENPAQUETADO DE TUPLAS - Asignar elementos de una tupla a diferentes variables
print("Desempaquetado de una tupla")
tupla1 = (0,52,"hola","aquellos",True)
a,b,c,d,e = tupla1
print(f"{a,b,c,d,e}\n")

#FUNCIONES INTEGRADAS CON TUPLAS
mi_tupla = (5,8,9,60,93,78,10)
print("Función 'len'")
print(f"{len(mi_tupla)}\n")
print("Función 'max'")
print(f"{max(mi_tupla)}\n")
print("Función 'min'")
print(f"{min(mi_tupla)}\n")
print("Función 'sum'")
print(f"{sum(mi_tupla)}\n")