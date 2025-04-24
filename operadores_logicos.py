# 5. Operadores lógicos

# Función para verificar si puede conducir
def verificar_conduccion():
    edad = int(input("Ingrese su edad: "))
    licencia = input("¿Tiene licencia de conducción? (si/no): ").lower()
    if edad >= 18 and licencia == "si":
        print("Puede conducir.")
    else:
        print("No puede conducir.")


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
    numero = int(input("Ingrese un número: "))
    if 10 <= numero <= 50:
        print(f"{numero} está en el rango de 10 a 50.")
    else:
        print(f"{numero} no está en el rango de 10 a 50.")
