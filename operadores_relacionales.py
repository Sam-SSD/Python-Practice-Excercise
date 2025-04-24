# 4. Operadores relacionales

# Función para comparar dos números
def comparar_numeros():
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        if num1 > num2:
            print(f"{num1} es mayor que {num2}.")
        elif num1 < num2:
            print(f"{num1} es menor que {num2}.")
        else:
            print(f"{num1} y {num2} son iguales.")
    except ValueError:
        print("Error: Debe ingresar números enteros válidos.")


# Función para verificar si una persona es menor o mayor de edad
def verificar_menor_edad():
    try:
        edad = int(input("Ingrese su edad: "))
        if edad < 0:
            print("La edad no puede ser negativa.")
        elif edad < 18:
            print("Eres menor de edad.")
        else:
            print("Eres mayor de edad.")
    except ValueError:
        print("Error: La edad debe ser un número entero.")


# Función para comparar dos cadenas
def comparar_cadenas():
    cadena1 = input("Ingrese la primera cadena: ")
    cadena2 = input("Ingrese la segunda cadena: ")
    if cadena1 == cadena2:
        print("Las cadenas son iguales.")
    else:
        print("Las cadenas son distintas.")
