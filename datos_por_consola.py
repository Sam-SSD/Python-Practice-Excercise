# 1. Ingreso de datos por consola

# Función para saludo personalizado
def saludo_personalizado():
    try:
        nombre = input("Ingrese su nombre: ")
        edad = int(input("Ingrese su edad: "))
        print(f"Hola {nombre}, tienes {edad} años.")
    except ValueError:
        print("Error: La edad debe ser un número entero.")


# Función para comida y color favorito
def comida_color_favorito():
    comida = input("Ingrese su comida favorita: ")
    color = input("Ingrese su color favorito: ")
    print(f"Tu comida favorita es {comida} y tu color favorito es {color}.")


# Función para calcular el doble y triple de un número
def doble_triple():
    try:
        numero = float(input("Ingrese un número: "))
        if numero < 0:
            print("El número debe ser positivo.")
        else:
            print("El doble de", numero, "es", numero * 2, "y el triple es", numero * 3)
    except ValueError:
        print("Error: El número debe ser un valor numérico.")
