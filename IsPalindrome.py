# Programa ver si una palabra es palindromo - Program to verify if a word is palindrome

def es_palindromo(palabra):
    return palabra.lower() == palabra.lower()[::-1]

palabras = []
palabras_lower = []

for i in range(5):
    # While True para asegurar que el usuario solo ingrese palabras validas
    while True:
        palabra = input(f"Introduce la palabra {i+1}: ")
        if not palabra.isalpha():
            print("Error: solo se permiten letras\n")
        elif len(palabra) < 2:
            print("Error: la palabra debe tener al menos dos letras\n")
        else:
            break # Con el break nos salimos del ciclo While True

    #Se vuleve la palabra en minusculas y se agrega a la lista palabras
    palabras.append(palabra)

print("\n")
for palabra in palabras:
    if es_palindromo(palabra):
        print(f"{palabra} es un palíndromo")
    else:
        print(f"{palabra} no es un palíndromo")