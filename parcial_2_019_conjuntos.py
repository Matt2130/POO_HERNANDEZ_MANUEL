frutas = {"Piña","Fresa","Higo","Manzana","Platano"}
frutas2 = {"Papaya","Uva","Durazno","Toronja","Naranja"}

union = frutas.union(frutas2)

union.add("Guayaba")

for i in union:
    print(i,end=" | ")