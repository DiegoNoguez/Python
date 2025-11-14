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



# Busqueda de subcadneas usando el metodo .find() es usado para 
# buscar una subcadena dentro de otra cadena y devuelve la posicion (indice) donde 
# empieza esa cadena y en caso de no encontrarla devuelve -1 
# ejemplo de como funciona este metodo 
# cadena.find(subcadena, inicio, fin)
# Donde subcadena es el texto a buscar 
#       inicio: indice donde comienza la busqueda
#       fin: indice dondee termina la busqueda y son opcionales

# Busqueda de la palabra o cadena como
pos2 = frase.find('como')

print(f'Posición de la palabra "como" : {pos2}')


# Remplazo de subcadenas 
# cadena.replace(textoBuscar, texto_nuevo)
# EJemplo 

frase1 = 'Hola mundo'
nuevaFras= frase1.replace('mundo', 'Pyhton')

print(f'Esta es la frase original {frase1}')
print(f'Esta es la frase con replace {nuevaFras}')