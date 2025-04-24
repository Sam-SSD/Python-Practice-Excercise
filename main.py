# Ejercicios de Python

# Importar funciones de los módulos
from datos_por_consola import saludo_personalizado, comida_color_favorito, doble_triple
from tipos_datos import tipos_basicos, convertir_cadena_a_entero, convertir_texto_a_flotante, es_numero
from operadores import area_rectangulo, precio_con_descuento, residuo_division, formula_con_operadores
from operadores_relacionales import comparar_numeros, verificar_menor_edad, comparar_cadenas
from operadores_logicos import verificar_conduccion, aplicar_oferta_trabajo, verificar_rango


# Menú de opciones
def menu():
    print("\n----------Menú de opciones----------")
    print("Seleccione una opción:")
    print("1. Ingreso de datos por consola")
    print("2. Tipos de datos en Python")
    print("3. Operadores en Python")
    print("4. Operadores relacionales")
    print("5. Operadores lógicos")
    print("6. Salir")
    print("-----------------------------------")

    opcion = input("Seleccione una opción: ")
    return opcion


# Programa principal
print("----------Bienvenido al programa de ejercicios de Python----------")
while True:
    opcion = menu()
    if opcion == "1":  # Ingreso de datos por consola
        saludo_personalizado()  # Saludo personalizado
        comida_color_favorito()  # Comida y color favorito
        doble_triple()  # Doble y triple de un número

    elif opcion == "2":  # Tipos de datos en Python
        tipos_basicos()  # Tipos básicos de datos
        convertir_cadena_a_entero()  # Convertir cadena a entero
        convertir_texto_a_flotante()  # Convertir texto a flotante
        cadena = input("Ingrese una cadena para verificar si es número: ")
        print(f"¿La cadena '{cadena}' es un número? {es_numero(cadena)}")

    elif opcion == "3":  # Operadores en Python
        area_rectangulo()  # Área de un rectángulo
        precio_con_descuento()  # Precio con descuento
        residuo_division()  # Residuo de una división
        formula_con_operadores()  # Fórmula con operadores

    elif opcion == "4":  # Operadores relacionales
        comparar_numeros()  # Comparar dos números
        verificar_menor_edad()  # Verificar menor de edad
        comparar_cadenas()  # Comparar cadenas

    elif opcion == "5":  # Operadores lógicos
        verificar_conduccion()  # Verificar si puede conducir
        aplicar_oferta_trabajo()  # Aplicar oferta de trabajo
        verificar_rango()  # Verificar rango de edad

    elif opcion == "6":
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida, intente nuevamente.")

print("----------Gracias por usar el programa----------")
