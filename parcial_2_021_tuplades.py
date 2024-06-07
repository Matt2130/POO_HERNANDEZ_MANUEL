datos = (18,"Manuel","Durango",1.78,"UTD")

a,b,c,d,e = datos

datos_generales = {
    "Edad":a,
    "Nomre":b,
    "Localidad":c,
    "Altura":d,
    "Estudios":e
}

for j,i in datos_generales.items():
    print(f"{j} es {i}")