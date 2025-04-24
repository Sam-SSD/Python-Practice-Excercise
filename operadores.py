# 3. Operadores en Python

# Función para calcular el área de un triángulo
def area_rectangulo():
    try:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))

        if base < 0 or altura < 0:
            print("debe ingresar valores positivos.")
        else:
            area = base * altura
            print(f"El área del rectángulo es {area}.")
    except ValueError:
        print("Error: La base y la altura deben ser números válidos.")


# Función para el descuento en un precio
def precio_con_descuento():
    try:
        precio = float(input("Ingrese el precio: "))
        descuento = float(input("Ingrese el porcentaje de descuento: "))
        if precio < 0 or descuento < 0:
            print("El precio y el descuento deben ser valores positivos.")
        else:
            if descuento > 100:
                print("El descuento no puede ser mayor al 100%.")
            else:
                precio_final = precio - (precio * descuento / 100)
                print(f"El precio final a pagar es {precio_final}.")
    except ValueError:
        print("Error: El precio y el descuento deben ser números válidos.")


# Función para calcular el residuo de una división
def residuo_division():
    try:
        num1 = int(input("Ingrese el primer número: "))
        num2 = int(input("Ingrese el segundo número: "))
        if num2 == 0 or num1 == 0:
            print("No se puede dividir entre cero.")
        else:
            residuo = num1 % num2
            print(f"El residuo de la división de {num1} entre {num2} es {residuo}.")
    except ValueError:
        print("Error: Debe ingresar números enteros válidos.")


# Función para calcular una fórmula con operadores
def formula_con_operadores():
    a = 5
    b = 10
    c = 2
    resultado = (a + b) * c - (b / a)
    print("\nel valor de a es 5")
    print("el valor de b es 10")
    print("el valor de c es 2")
    print("La formula es (a + b) * c - (b / a)")
    print(f"El resultado de la fórmula es {resultado}.")
