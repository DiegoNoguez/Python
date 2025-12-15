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

# Eliminar elementos de una lista
# usando el metodo remove 
mi_lista.remove(5)
print(f'{mi_lista} Se removio el valor 5 mas no el indice')

# remover por indice con el metodo pop 
mi_lista.pop(1) # Remueve el elemento del indice 1
print(f'{mi_lista} Se elimino el indice 1')

# Eliminar usando la palabra del
del mi_lista[2]
print(f'{mi_lista} Se elimino el indice 2 de la lista')

# Obtener sublistaas
sublista = mi_lista[:3] # obtiene el indice 0 al 2
print(f'{sublista} La sublista contiene los indices de 0 al 2')
