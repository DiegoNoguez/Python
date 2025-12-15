# Ejemeplo de impresion en mensaje en funcion in range 
print(" Impresion de mensaja")

mensaje = input("Ingresa un mensaje: ")
num_repeticiones = int(input("Ingresa el numero de repeticiones: "))
for i in range(num_repeticiones):
    print(f'{i+1}.- {mensaje}')