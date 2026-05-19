"""
El presente algoritmo propone solucionar el realizar un promedio 
de calificaciones mediante el uso de colecciones en python
""" 

# variables
calificaciones = []
espacio = "*" *3

print(f'{espacio}Promedio de calificaciones{espacio}')
total_cal = int(input(f'Poroporciona el numero de calificaciones: '))

# iteracion con ciclo for 
for indice in range(total_cal):
    calificacion = float(input(f'Ingresa la calificacion correspondiente a {indice}: '))
    calificaciones.append(calificacion)

# impresion de califiacion
print(f'Las calificaciones dadas son:\n {calificaciones}')

# calcculo del proemedio 
prom = sum(calificaciones) 
promedio = (prom/total_cal)
print(f'El promedio de las califiaciones son: {promedio}')