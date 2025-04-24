# 1. Ingreso de datos por consola

# Función para saludo personalizado
def saludo_personalizado():
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")
    print(f"Hola {nombre}, tienes {edad} años.")


# Función para comida y color favorito
def comida_color_favorito():
    comida = input("Ingrese su comida favorita: ")
    color = input("Ingrese su color favorito: ")
    print(f"Tu comida favorita es {comida} y tu color favorito es {color}.")


# Función para calcular el doble y triple de un número
def doble_triple():
    numero = float(input("Ingrese un número: "))
    print(f"El doble de {numero} es {numero * 2} y el triple es {numero * 3}.")
