# Calculadora de propinas - Tip Calculator 

factura_total = float(input("Por favor ingrese cual es la factura total de hoy: $"))

while True:
    opcion = input("\nElija el porcentaje de propina que desea aplicar: \n1. 18% \n2. 20% \n3. 25% \n")
    if opcion == "1":
        porcentaje_propina = 0.18
        break
    elif opcion == "2":
        porcentaje_propina = 0.20
        break
    elif opcion == "3":
        porcentaje_propina = 0.25
        break
    else:
        print("Opción no válida. Por favor, elija 1, 2 o 3.")

propina = round(factura_total * porcentaje_propina, 2)
total_con_propina = round(factura_total + propina, 2)

print(f"\nLa propina aplicando el {porcentaje_propina*100}% es ${propina}, que contabiliza un total de ${total_con_propina}")

while True:
    num_personas = int(input("\n¿Cuántas personas van a compartir la factura? "))
    if num_personas <= 0:
        print("Error: el número de personas debe ser mayor que cero")
    else:
        break

while True:
    opcion = input("¿Quieres dividir la factura de manera equitativa o desigual? (E/D) ")
    if opcion.lower() == "e":
        costo_persona = round(total_con_propina / num_personas, 2)
        print(f"Cada persona debe pagar ${costo_persona}")
        break
    elif opcion.lower() == "d":
        porcentajes = []
        total_porcentaje = 0
        for i in range(num_personas):
            while True:
                porcentaje = float(input(f"Introduce el porcentaje que pagará la persona {i+1}: "))
                if porcentaje < 0 or porcentaje > 100:
                    print("Error: el porcentaje debe estar entre 0 y 100")
                else:
                    break
            porcentajes.append(porcentaje)
            total_porcentaje += porcentaje
        
        for i in range(num_personas):
            costo_persona_i = round(total_con_propina * porcentajes[i] / 100 / (num_personas - 1), 2)
            print(f"La persona {i+1} debe pagar ${costo_persona_i}")
        break
    else:
        print("Error: opción no válida")

print("\n¡Gracias por utilizar nuestra calculadora de propinas!")