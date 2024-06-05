def clear_screen():
    print("\033c", end="")
    
while True:
    print("MENU:\n")
    print("CONVERSIÓN DE TEMPERATURAS")
    print("1. De Celcius a Fahrenheit")
    print("2. De Fahrenheit a Celcius")
    print("3. Salir del programa\n")
    opcion = input("Ingrese la opción que desea ejecutar ( 1 | 2 | 3 ) : ")
    
    if opcion == "1":
       clear_screen()
       DeCaF = float(input("Ingrese los °C para convertirlos a °F: "))
       opCaF = ((DeCaF * 9/5) + 32)
       redondeoC = round(opCaF,2)
       print(f"Los {DeCaF} °C equivalen a {redondeoC} °F") 
    elif opcion == "2":
        clear_screen()
        DeFaC = float(input("Ingrese los °F para convertirlos a °c: "))
        opFac = ((DeFaC - 32) * 5/9 )
        redondeoF = round(opFac,2)
        print(f"Los {DeFaC} °C equivalen a {redondeoF} °F")
    elif opcion == "3":
        clear_screen()
        print("Saliendo del programa....")
        break
    else:
        clear_screen()
        print("Dato invalido. Ingrese 1 | 2 | 3 ")

        