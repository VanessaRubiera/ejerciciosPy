# WordCount

# Se ingresa un string
text = input("Ingresa una oración: ")

# Contar el número de palabras, y separarlas con split, el separador por default es el espacio
number_words = len(text.split())

print(f"La oración que has ingresado : \'{text}\' tiene {number_words} palabras.")
