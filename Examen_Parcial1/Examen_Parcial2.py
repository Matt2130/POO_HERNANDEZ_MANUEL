import math

def clear_screen():
    print("\033c", end="")
    
def rectangle(base_rectangle, height_rectangle):
    area_rectangle = base_rectangle * height_rectangle
    average_rectangle = round(area_rectangle,2)
    return average_rectangle

def triangle(base_triangle, height_triangle):
    area_triangle = (base_triangle * height_triangle) / 2
    average_triangle = round(area_triangle,2)
    return average_triangle

def circle(radio):
    area_circle = math.pi * (radio*radio)
    average_circle = round(area_circle,2)
    return average_circle 

def menu():
    print("MENU:")
    print("Choose an option to find out the area of these figures: ")
    print("a) Rectangle")
    print("b) Triangle")
    print("c) Circle")
    print("d) Exit ")

clear_screen()

while True:  
    menu()
    x = input("Option: ")
    if x == "a":
        base_rectangle = float(input("\nEnter the base of rectangle: "))
        height_rectangle = float(input("Enter the height of rectangle: "))
        clear_screen()
        print(f"The area of rectangle is {rectangle(base_rectangle, height_rectangle)}\n")            
    elif x == "b":
        base_triangle = float(input("\nEnter the base of triangle: "))
        height_triangle = float(input("Enter the height of triangle: "))
        clear_screen()
        print(f"The area of triangle is {triangle(base_triangle, height_triangle)}\n")
    elif x == "c":
        radio = float(input("\nEnter the radio of the circumference: "))
        clear_screen()
        print(f"The area of circle is {circle(radio)}\n")
    elif x == "d":
        clear_screen()
        print("Exit the program ...")
        break 
    else:
        clear_screen()
        print("Plese. Enter a correct letter")