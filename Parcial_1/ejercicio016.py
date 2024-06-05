prom1 = float((input("Ingrese un promedio: ")))
prom2 = float((input("Ingrese otro promedio: ")))
prom3 = float((input("Ingrese otro promedio: ")))

prom1,prom2,prom3

if prom1 > prom2 and prom1 > prom3:
    print(f"El promedio más alto de los ingresados es de {prom1}")
elif prom2 > prom1 and prom2 > prom3:
    print(f"El promedio más alto de los ingresados es de {prom2}")    
else:
    print(f"El promedio más alto de los ingresados es de {prom3}")