#Acronym

# Pedir al usuario que ingrese una oracion
significado = input("Por favor ingresa una oración: ")

# Convertir el significado en un acrónimo
acrónimo = ''.join(word[0].upper() for word in significado.split())

# Imprimir el acrónimo
print("El acrónimo de '" + significado + "' es: " + acrónimo)