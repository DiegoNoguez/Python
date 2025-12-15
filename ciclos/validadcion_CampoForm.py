# validadacion de un campo de un formulario 

print(" Validación de campo de un Formulario. ")

nombre_usuario = None

while not nombre_usuario:
    nombre_usuario = input("Ingresa tu nombre de usuario: ")

print(f'Nombre de usuario valido: {nombre_usuario}')