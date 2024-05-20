peso = float(input("Ingrese el peso de su paquete en kg: "))

if peso < 1:
    print("El costo de su envío es de $50")
elif peso < 5:
    print("El costo de su envío es de $100")
elif peso < 10:
    print("El costo de su envío es de $200")  
else:
    print("El costo de su envío es de $500")