#Juego de Piedra, Papel o Tijera - Game Rock, Paper or Scissors
import random

print("Juego de Piedra, Papel o Tijera!")
print("Selecciona tu opción:")
print("1. Piedra")
print("2. Papel")
print("3. Tijera\n")

options = ["Piedra", "Papel", "Tijera"]
player_choice = int(input("Ingresa tu opción (1-3): "))
computer_choice = random.randint(1, 3)

print("\nTú elegiste:", options[player_choice-1])
print("La computadora eligió: ", options[computer_choice-1], "\n")

if player_choice == computer_choice:
    print("Empate!")
elif player_choice == 1 and computer_choice == 2:
    print("Perdiste! Papel envuelve Piedra.")
elif player_choice == 1 and computer_choice == 3:
    print("Ganaste! Piedra aplasta Tijera.")
elif player_choice == 2 and computer_choice == 1:
    print("Ganaste! Papel envuelve Piedra.")
elif player_choice == 2 and computer_choice == 3:
    print("Perdiste! Tijera corta Papel.")
elif player_choice == 3 and computer_choice == 1:
    print("Perdiste! Piedra aplasta Tijera.")
elif player_choice == 3 and computer_choice == 2:
    print("Ganaste! Tijera corta Papel.")