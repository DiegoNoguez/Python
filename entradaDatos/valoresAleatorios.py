# Generacion de valores aleatorios en python usanddo randint()
# recibe dos parametros entre los valores a y b 
from random import randint # para usar la funcion de randint

# Generación de un numero aleatorio
numero = randint(1,20) # a no puede ser mayor a b 
print(f'El numero aleatorio en un rango de 1-20 es: {numero}')


# SImulacion de un dado de 6 caras
dado =randint(1,6)
print(f'\nEl valor del dado es: {dado}')