"""
Docstring for ciclos.cajeroAuto
Ejercicio: Desarroillar un cajero auromatico dentro de las cuales tendra
como funciones principales de un cajero, deposito, retiro, consultar el saldo.,
 saldo minimo es de 1000
"""

print("<--- Aplicación de Cajero Automatico --->")

salida = False 
while not salida:
    print(''' Operaciones que puedes realizar:
          1.- Consultar Saldo
          2.- Retirar
          3.- Depositar
          4.- Salir''')
    opcion = int(input("Escoge una opción a realizar: "))