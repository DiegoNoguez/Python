"""RETO 
    Sistema Generador de ID ÚNICO 
    Se solicita crear un sistema para generar un ID
    único para cada persona 
        El sistema debe solicitar al usuario 
            Nombre
            Apellido 
            Año de naciemto 
    Con los datos recibidos de nombre solo se usaura las 2 primeras letras y convertirlas
    a minusculas, del apellido lo mismo pero con mayusculas 
    y del año solo tomar los dos ultimos digitoa y generar 4 digitos finales con randint
    """
from random import randint
print(f'<---- Sistema Generador de ID único ---->')
nombre = input("Ingresa tu nombre: ")
apllido = input ("Ingresa tu apellido: ")
yearNata= input("Ingresa tu año de nacimiento: ")

# desarrollo de logica
nombreFinal = nombre[:2].upper()
apellidoFinal = apllido[:2].upper()
yearFinal = yearNata[2:4]
numeroAle = str(randint(1000,5600))
numeroId = nombreFinal + apellidoFinal + yearFinal +numeroAle

# impresion del mensaje
print(f'Hola {nombre}')
print(f'\tTu nuevo ID generado por el sistema es:')
print(f'\t{numeroId}')
print(f'\t!Felicidades¡')