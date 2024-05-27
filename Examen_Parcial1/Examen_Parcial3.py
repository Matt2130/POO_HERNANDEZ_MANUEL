edades_generales = [21,8,7,8,6,11,17,26,18,19,9,10,78,52,8,13,10,52,30,74,10,21,63,32]

edad_infancia = []
edad_adol = []
edad_jov = []
edad_adult = []

edades_generales.sort()
print(f"\nLa lista con todas las edades es {edades_generales}")

for i in edades_generales:
    if i >= 6 and i <= 11:
        edad_infancia.append(i)
    elif i >= 12 and i <= 17:
        edad_adol.append(i)
    elif i >= 18 and i <= 26:
        edad_jov.append(i)
    else:
        edad_adult.append(i)
        
edad_infancia.sort()        
print(f"\nLa lista con las edades que se encuentran en la infancia es {edad_infancia}")

edad_adol.sort()
print(f"\nLa lista con las edades que se encuentran en la adolescencia es {edad_adol}")

edad_jov.sort()
print(f"\nLa lista con las edades que se encuentran en la juventud es {edad_jov}")

edad_adult.sort()
print(f"\nLa lista con las edades que se encuentran en la adultez es {edad_adult}")