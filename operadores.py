# 3. Operadores en Python

# Función para calcular el área de un triángulo
def area_rectangulo():
    base = float(input("Ingrese la base del rectángulo: "))
    altura = float(input("Ingrese la altura del rectángulo: "))
    area = base * altura
    print(f"El área del rectángulo es {area}.")


# Función para el descuento en un precio
def precio_con_descuento():
    precio = float(input("Ingrese el precio: "))
    descuento = float(input("Ingrese el porcentaje de descuento: "))
    precio_final = precio - (precio * descuento / 100)
    print(f"El precio final a pagar es {precio_final}.")


# Función para calcular el residuo de una división
def residuo_division():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    residuo = num1 % num2
    print(f"El residuo de dividir {num1} entre {num2} es {residuo}.")


# Función para calcular una fórmula con operadores
def formula_con_operadores():
    a = 5
    b = 10
    c = 2
    resultado = (a + b) * c - (b / a)
    print("el valor de a es 5")
    print("el valor de b es 10")
    print("el valor de c es 2")
    print("La formula es (a + b) * c - (b / a)")
    print(f"El resultado de la fórmula es {resultado}.")
