# 5. Operadores lógicos

# Función para verificar si puede conducir
def verificar_conduccion():
    try:
        licencia = input("¿Tiene licencia de conducción? (si/no): ").lower()
        edad = int(input("Ingrese su edad: "))
        if edad < 0:
            print("La edad no puede ser negativa.")
        elif licencia == "si" and edad >= 18:
            print("Puede conducir.")
        elif licencia == "no" and edad >= 18:
            print("No puede conducir sin licencia.")
        elif licencia == "si" and edad < 18:
            print("No puede conducir, es menor de edad.")
        elif licencia != "si" and licencia != "no":
            print("Error: Respuesta inválida. Debe ingresar 'si' o 'no'.")
        elif licencia == "no" and edad < 18:
            print("No puede conducir, es menor de edad y no tiene licencia.")
    except ValueError:
        print("Error: La edad debe ser un número entero.")


# Función para aplicar a una oferta de trabajo
def aplicar_oferta_trabajo():
    experiencia = input("¿Tiene experiencia laboral? (si/no): ").lower()
    titulo = input("¿Tiene título universitario? (si/no): ").lower()
    if experiencia == "si" and titulo == "si":
        print("Puede aplicar a la oferta de trabajo.")
    else:
        print("No puede aplicar a la oferta de trabajo.")


# Función para verificar si un número está en un rango entre 10 y 50
def verificar_rango():
    try:
        numero = int(input("Ingrese un número (10-50): "))
        if numero < 10 or numero > 50:
            print("El número no está en el rango de 10 a 50.")
        else:
            print("El número está en el rango de 10 a 50.")
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")