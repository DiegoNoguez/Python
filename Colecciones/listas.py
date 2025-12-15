print('Manejo de listas')
mi_lista = [1,2,3,4,5]
print(f'{mi_lista} Esta es la lista original')

# Obtencion de lo largo de una lista
print(f'El largo de la lista es: {len(mi_lista)}')

#Acceder a los elementos de la lista por indice 
print(f'Accedemos al valor del indice: {mi_lista[4]}') # Tambien se puede manejar de forma negativa

# Modificar los elementos de una lista 
mi_lista[1] = 10
print(f'Modificamos el valor del indice 1: {mi_lista[1]}')

#Agregar un nuevo elemento al final de la lista 
mi_lista.append(6)
print(f'{mi_lista} Se agrego el elemento 6')

# cON INSERT UN NUEVO ELEMENTO ESPECIFICO 
mi_lista.insert(2,15)
print(f'{mi_lista} Se añadio el valor de 15 en el indice 2')
