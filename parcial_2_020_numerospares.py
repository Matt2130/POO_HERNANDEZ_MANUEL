print("Los tres conjutos son:\n")
conjunto1 = {1,8,9,85,9,6,3,114,5,2,9,3,32,5,6,9,85,7,4,25,69,2}
print(f"{conjunto1}\n")
conjunto2 = {45,986,22,3,20,10,36,985,74,632,8,63,210,3,82}
print(f"{conjunto2}\n")
conjunto3 = {2,5,895,310,254,32,1,10,2,5,863,300,84,6983,62,143}
print(f"{conjunto3}\n")

conjunto_union = conjunto1.union(conjunto2)
conjunto_union = conjunto1.union(conjunto3)
print("La union de los tres conjuntos es:")
print(f"{conjunto_union}")
print(f"El total de elementoss en este conjunto es de {len(conjunto_union)}\n")

for i in conjunto_union:
    if i % 2 == 0:
        print(f"El número {i} es par")