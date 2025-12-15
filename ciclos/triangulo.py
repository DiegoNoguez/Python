# Dibujo de un triangulo simetrico 
print(f' Dibujar triangulo simetrico ')

numero_filas = int(input("Proporciona el número de filas: "))

# Iterar sobre cada fila del triángulo 
for fila in range(1, numero_filas+1):
    espacio_blanco = ' ' * (numero_filas-fila)
    astericos = '*' * (2*fila-1)
    print(f'{espacio_blanco}{astericos}')