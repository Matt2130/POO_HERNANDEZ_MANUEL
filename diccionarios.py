invenario = {
    "Carne":65,
    "Leche":41,
    "Azúcar":23,
    "Jabón":10,
    "Huevo":80,
    "Refresco":15,
    "Manzana":20
}

#Código para aplicar el descuento a cada uno de los productos por separado
#for key,values in invenario.items():
#    print(f"{key} = {values}")  
#for key,value in invenario.items():
#    invenario_nuevo = int(input(f"\nIngrese el descuento del producto {key} (del 1% al 100%): "))
#    descuento = (value-((invenario_nuevo/100) * value))
#    descuento_redo = round(descuento,2)
#    print(f"El precio original de la {key} = {value}")
#    print(f"El precio ya con el descuento aplicado es de {key} = {descuento_redo}")

for key,value in invenario.items():
    print(f"{key} = {value}")
    
invenario_nuevo = int(input(f"\nIngrese el descuento que se le aplicaran a todos los productos (del 1% al 100%): "))
print("")

for key,value in invenario.items():
    descuento = (value-((invenario_nuevo/100) * value))
    descuento_redo = round(descuento,2)
    print(f"El precio original del producto '{key}' es de {value}")
    print(f"El precio ya con el descuento aplicado para el producto '{key}' es de {descuento_redo}\n")