edades = [2,5,76,8,10,58,63,14,18,20,75,63,9]
may_edad = []
men_edad = []

print(f"\fLa lista con todas las edades es {edades}")

for i in edades:
    if i <= 17: 
        men_edad.append(i)
    else:
        may_edad.append(i)
        
print(f"\nLa lista con las edades menor de edad es {men_edad}")
print(f"La lista con las edades mayor de edad es {may_edad}\n")