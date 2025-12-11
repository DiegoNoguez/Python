# Creacion de un menu iterativo usandi ciclos mandando solo mensajes genericos 

print(" Menu iterativo ")

salir = False
while not salir:
    print(f''' MENU:
          1.- Crear Cuenta 
          2.- Eliminar Cuenta
          3.- Salir ''')
    opcion = int(input("Escoge una opción: "))
    if opcion == 1:
        print("Creando tu cuenta \n")
    elif opcion == 2:
        print("Eliminando la cuenta\n")
    else:
        print("Saliendo del sistema \n")
        salir = True