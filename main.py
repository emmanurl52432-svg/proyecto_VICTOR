while True:
    try:
        cuenta = float(input("¿Cuánto fue la cuenta? $"))
        break
    except ValueError:
        print("Por favor, ingrese un número válido para la cuenta.")

historial = []
seguir = True

while seguir:
    print('---------------------------------')
    print("¿Qué desea hacer con la cuenta?:")
    print("1. Dividir la cuenta entre varias personas")
    print("2. Calcular propina a la cuenta")
    print("3. Ver historial")
    print("4. Salir")
    print ('-------------------------------')
    while True:
        try:
           opcion = int(input("Ingrese el número de la opción que desea: "))
           break
        except ValueError:
         print("por favor, ingrese un Numero valido para la opcion"
               )

    if opcion == 1:
        personas = int(input("Ingrese el número de personas: "))
        total_por_persona = cuenta / personas
        print(f"Cada persona debe pagar: ${total_por_persona}"
              )

    elif opcion == 2:
        porcentaje_propina = float(input(
            "Ingrese el porcentaje del total que desea dejar de propina" \
            " "))
        propina = cuenta * (porcentaje_propina / 100)
        print(f"La propina a dejar es: ${propina}"
              )

        print("¿Desea cambiar el porcentaje de propina? s/n")
        if input().lower() == "s":
            porcentaje_propina = float(input("Ingrese el nuevo porcentaje de propina:" \
            " "))
            propina = cuenta * (porcentaje_propina / 100)
            print(f"La nueva propina a dejar es: ${propina}"
                  )

        historial.append({"cuenta": cuenta, "propina": propina})

    elif opcion == 3:
        if not historial:
            print("No cuenta con historial de cuentas." \
            "")
        else:
            print("Historial de cuentas:")
            for registro in historial:
                print(f"Cuenta: ${registro['cuenta']}, Propina: ${registro['propina']}")

    elif opcion == 4:
        print("Saliendo del programa...")
        seguir = False
    else: 
        print('opcion no valida, por favor ingresa una opcion del 1 al 4') 
    

    

        
        
        

