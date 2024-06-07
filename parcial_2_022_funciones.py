def limpiar():
    print("\033c", end="")
    
def suma(num1,num2):
    result1 = num1 + num2
    return result1

def resta(num1,num2):
    result1 = num1 - num2
    return result1

def mult(num1,num2):
    result1 = num1 * num2
    return result1

def division(num1,num2):
    result1 = num1 / num2
    redondeo = round(result1,2)
    return redondeo

menu = ["1) Suma", "2) Resta", "3) Multiplicación", "4) División", "5) Salir"]

limpiar()

while True:
    print("CALCULADORA")
    print("Seleccione la opción para ejecutar la operción")
    for i in menu:
        print(f"|  {i}  |")
        print("------------------------")
    opcion = input("Ingrese la opción: ")
    
    if opcion == "1":
        limpiar()
        print("SUMA")
        num1 = float(input("Ingrese un número: "))
        num2 = float(input("Ingrese otro número: "))
        print(f"El resultado de la suma es {suma(num1,num2)}\n")
    elif opcion == "2":
        limpiar()
        print("RESTA")
        num1 = float(input("Ingrese un número: "))
        num2 = float(input("Ingrese otro número: "))
        print(f"El resultado de la resta es {resta(num1,num2)}\n")
    elif opcion == "3":
        limpiar()
        print("MULTIPLICACIÓN")
        num1 = float(input("Ingrese un número: "))
        num2 = float(input("Ingrese otro número: "))
        print(f"El resultado de la multiplicación es {mult(num1,num2)}\n")
    elif opcion == "4":
        limpiar()
        print("DIVISIÓN")
        num1 = float(input("Ingrese un número: "))
        num2 = float(input("Ingrese otro número: "))
        print(f"El resultado de la división es {division(num1,num2)}\n")
    elif opcion == "5":
        print("Saliendo...")
        break
    else:
        print("Dígito no valido. Ingrese uno valido.")