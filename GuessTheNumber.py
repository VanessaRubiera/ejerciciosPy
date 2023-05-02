# Programa adivina el numero - Guess the number

import random

numero_oculto = random.randint(1,50)
num_intentos = 0
continuar_jugando = True

while continuar_jugando:
    num_intentos += 1
    num_usuario = int(input("\nIntroduce un número entre 1 y 50: "))

    if num_intentos >= 10:
        print(f"\nOh, ya lo has intentado muchas veces, el numero oculto era {numero_oculto}.")
        respuesta = input("\n¿Quieres seguir jugando? (s/n)")
        if respuesta.lower() == "s":
            numero_oculto = random.randint(1,50)
            num_intentos = 0
        else:
            continuar_jugando = False
    else:
        if num_usuario < 1 or num_usuario > 50:
            print("Error: el número debe estar entre 1 y 50")
        elif num_usuario < numero_oculto:
            print("El número oculto es mayor")
        elif num_usuario > numero_oculto:
            print("El número oculto es menor")
        else:
            print("\n¡Felicidades, has adivinado el número oculto en", num_intentos, "intentos!")
            respuesta = input("\n¿Quieres seguir jugando? (s/n)")
            if respuesta.lower() == "s":
                numero_oculto = random.randint(1,50)
                num_intentos = 0
            else:
                continuar_jugando = False

print("Gracias por jugar!")