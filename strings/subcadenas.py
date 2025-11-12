# Subcadenas en python 
# la forma de obtenerlas es usando slicing es [inicio:fin] como si manejaramos arrays

frase = 'hOLa como estas'

# Inicio de la extracción de la subcadena
subcadena = frase[0:4]
print(f'Frase completa:{frase}')
print(f'La subcadeana es: {subcadena}')

# python no cuenta el ultimo indice

# ejmplo mas directo
correo = 'beto@mail.com.mx'
indiceArroba = correo.index('@')
print(f'Valor de arroba por obtencion de indice {indiceArroba}')
usuario = correo[:correo.index('@')]
print(f'Nombre de Usuario {usuario}')

