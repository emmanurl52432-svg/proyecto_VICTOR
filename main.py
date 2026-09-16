def pedir_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido.")


def pedir_opcion(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingrese un número válido para la opción.")


def mostrar_menu():
    print('---------------------------------')
    print("¿Qué desea hacer con la cuenta?:")
    print("1. Dividir la cuenta entre varias personas")
    print("2. Calcular propina a la cuenta")
    print("3. Ver historial")
    print("4. Salir")
    print('-------------------------------')


def dividir_cuenta(cuenta, personas):
    return cuenta / personas


def calcular_propina(cuenta, porcentaje):
    return cuenta * (porcentaje / 100)


def mostrar_historial(historial):
    if not historial:
        print("No cuenta con historial de cuentas.")
    else:
        print("Historial de cuentas:")
        for registro in historial:
            print(f"Cuenta: ${registro['cuenta']}, Propina: ${registro['propina']}")


# ---------- PROGRAMA PRINCIPAL ----------

cuenta = pedir_numero("¿Cuánto fue la cuenta? $")
historial = []
seguir = True

while seguir:
    mostrar_menu()
    opcion = pedir_opcion("Ingrese el número de la opción que desea: ")

    if opcion == 1:
        personas = int(pedir_numero("Ingrese el número de personas: "))
        total_por_persona = dividir_cuenta(cuenta, personas)
        print(f"Cada persona debe pagar: ${total_por_persona}")

    elif opcion == 2:
        porcentaje_propina = pedir_numero(
            "Ingrese el porcentaje del total que desea dejar de propina, por ejemplo 15: "
        )
        propina = calcular_propina(cuenta, porcentaje_propina)
        print(f"La propina a dejar es: ${propina}")

        print("¿Desea cambiar el porcentaje de propina? s/n")
        if input().lower() == "s":
            porcentaje_propina = pedir_numero("Ingrese el nuevo porcentaje de propina: ")
            propina = calcular_propina(cuenta, porcentaje_propina)
            print(f"La nueva propina a dejar es: ${propina}")

        historial.append({"cuenta": cuenta, "propina": propina})

    elif opcion == 3:
        mostrar_historial(historial)

    elif opcion == 4:
        print("Saliendo del programa...")
        seguir = False

    else:
        print('Opción no válida, por favor ingresa una opción del 1 al 4')
    

    

        
        
        

