#Conjuntos 

#¿Qué son?
#Estos son una colección no ordenada de elementos únicos. Se utilizan al almacenar múltiples elementos sin duplicados y cuando no importa el orden de los elementos.

#Acciones comunes
#Creación - Utilizando llaves 
#conjunto = {valor,valor,valor} 
print("Creación de los conjuntos")
conjunto1 = {"azul", "amarillo", "rojo", "globo", "pony"}
conjunto2 = {"leon","carne","azul","jugo","globo","resorte"}
print(f"{conjunto1}\n")

#Añadir elementos
#método add()
#conjunto.add(valorNuevo)
print("Añade solo un elemento al conjunto")
conjunto1.add("hola")
print(f"{conjunto1}\n")

#Eliminar Elementos
#método remove()
#conjunto.remove(valor) error
#conjunto.discard(valor)
print("Eliminan elementos de la lista 'remove' (tiene que estar en el conjunto) y 'discard' (no es necesario que este)")
conjunto1.remove("pony")
conjunto1.discard("negro")
print(f"{conjunto1}\n")

#Operaciones
#unión de conjuntos
#unión = conjunto 1 | conjunto 2
#unión = conjunto1.union(conjunto2)
print("Unión de conjuntos por medio de una nueva variable")
n_union = conjunto1.union(conjunto2)
print(f"{n_union}\n")

#Intersección de conjuntos
#Une los elementos iguales de dos conjuntos
#intersección = conjunto 1 y conjunto 2
#intersección = conjunto.interseccion(conjunto2)
print("Une los elementos iguales de un par de conjuntos")
interseccion = conjunto1.intersection(conjunto2)
print(f"{interseccion}\n")

#diferencia de conjuntos
#Une los elementos que estan en el primer conjunto pero no en el segundo
#diferencia = conjunto1 - conjunto2
print("Pone los elememntos que no esten repetidos, pero solo imprime los del primer conjunto")
diferencia = conjunto1.difference(conjunto2)
print(f"{diferencia}\n")

#Metodos comunes
#numero de elemntos en el conjunto
#len(conjunto)
print("Cuent todos los elementos de un conjunto")
print(len(conjunto1))
print(f"{len(conjunto2)}\n")

#verifica si un elemnto esta en el conjunto
#in
#print("<valor a buscar>" in conjunto1)
print("Identifica si el elemento que se quiere buscar existe en la lista")
print("globo" in conjunto1)
print("negro" in conjunto2)
print("")

#Elimina todos los elementos del conjunto
#clear()
#conjunto.clear()
print("Limpia todo el conjunto (sus elementos) que se le indique")
print("conjunto1.clear()")
print(f"print(conjunto1)\n")

#devuelve una copia superficial del conjunto
#copy()
print("Da una copia de todo el conjunto")
conjunto1.copy()
print(f"{conjunto1}\n")