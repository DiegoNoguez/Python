""" 
    RETO DE RECETA DE COCINA 
    Crear un programa para solicitar algunos valores importantes para 
    una receta de cocina
    Los valores que debe introducir el usuario son :
        Nombre de la receta 
        Ingredientes 
        Tiempo de preparación 
        dificultad ('FACIL, MEDIANA, ALTA')

    Mandar a imprimir la receta 
"""

# gestion para impresion del ejercicio 
varGuion = "-"
varGuion = varGuion * 3
print(f'{varGuion} Receta de cocina {varGuion}')
nomReceta = input("Nombre de receta: ")
ingredientes = input("Ingres tus ingredientes: ")
tiempo = int(input("Ingresa el timepo expresado en minutos: "))
dificult  = input("Ingresa la dificultad: ")
varGuion = varGuion * 5
print(f'{varGuion}{varGuion}')
print(f'Nombre de la receta {nomReceta}')
print(f'Ingredientes: {ingredientes}')
print(f'Tiempo de preparación: {tiempo} minutos')
print(f'Dificultad: {dificult}')