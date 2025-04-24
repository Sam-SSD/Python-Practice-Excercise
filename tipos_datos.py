# 2. Tipos de datos en Python

# Función para mostrar tipos básicos de datos
def tipos_basicos():
    entero = 10
    flotante = 10.5
    cadena = "Hola"
    booleano = True
    print(f"Entero: {entero}, Flotante: {flotante}, Cadena: {cadena}, Booleano: {booleano}")


# Función para convertir una cadena a entero
def convertir_cadena_a_entero():
    cadena_numero = "20"
    numero = int(cadena_numero)
    suma = numero + 5
    print(f"La suma de {numero} y 5 es {suma}.")


# Función para convertir texto a flotante y multiplicar por 2
def convertir_texto_a_flotante():
    try:
        texto = input("Ingrese un número: ")
        numero_flotante = float(texto)
        if numero_flotante < 0:
            print("El número debe ser positivo.")
        else:
            resultado = numero_flotante * 2
            print(f"El resultado de multiplicar {numero_flotante} por 2 es {resultado}.")
    except ValueError:
        print("Error: Debe ingresar un número válido.")

# Función para verificar si una cadena es un número
def es_numero(cadena):
    try:
        float(cadena)
        return True
    except ValueError:
        return False
