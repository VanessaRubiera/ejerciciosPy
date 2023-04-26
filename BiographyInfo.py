# Biography Info

# Pedir al usuario su información personal
# Validar la información ingresada por el usuario
print("Por favor ingrese su información personal a continuación:")
nombre = input("Nombre completo: ")
while not nombre.isalpha():
    nombre = input("Por favor ingrese un nombre válido (sólo letras): ")
apellido = input("Apellido completo: ")
while not apellido.isalpha():
    apellido = input("Por favor ingrese un apellido válido (sólo letras): ")
edad = input("Edad: ")
while not edad.isdigit():
    edad = input("Por favor ingrese una edad válida (sólo números enteros): ")
direccion = input("Dirección: ")
email = input("Correo electrónico: ")
while "@" not in email:
    email = input("Por favor ingrese un correo electrónico válido: ")
telefono = input("Número de teléfono: ")
while not telefono.isdigit() or len(telefono) != 10:
    telefono = input("Por favor ingrese un número de teléfono válido (10 dígitos): ")
    
print("Resumen de la información personal:")
print(f"Nombre completo: {nombre.capitalize()} {apellido.capitalize()}")
print(f"Edad: {edad}")
print(f"Dirección: {direccion}")
print(f"Correo electrónico: {email}")
print(f"Número de teléfono: ({telefono[:3]}) {telefono[3:6]}-{telefono[6:]}")