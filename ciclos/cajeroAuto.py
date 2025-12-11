"""
Docstring for ciclos.cajeroAuto
Ejercicio: Desarroillar un cajero auromatico dentro de las cuales tendra
como funciones principales de un cajero, deposito, retiro, consultar el saldo.,
 saldo minimo es de 1000
"""

print("<--- Aplicación de Cajero Automatico --->")

SALDO = 1000
salida = False 
while not salida:
    print(''' Operaciones que puedes realizar:
          1.- Consultar Saldo
          2.- Retirar
          3.- Depositar
          4.- Salir''')
    opcion = int(input("Escoge una opción a realizar: "))
    if opcion == 1:
        print(f'Su saldo actual es de: {SALDO}\n')
    elif opcion == 2:
        retiro = int(input("Ingresa el monto a retirar: "))
        if retiro <= SALDO:
            print(f'EL retiro fue exitoso')
            print(f'La cantidad a retirar fue de: {retiro}')
        else:
            print(f'No cuentas con el saldo suficiente en la cuenta para hacer el retiro')
            print(f'Tu saldo actual es de: {SALDO}\n')
    elif opcion == 3:
        deposito = int(input("Ingresa la cantidad a depsoistar: "))
        SALDO +=deposito
        print("\n")
    elif opcion == 4:
        print(f'Saliendo de la aplicación bancanria')
        salida = True
print()