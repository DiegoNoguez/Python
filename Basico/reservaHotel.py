"""
Crear un sistema de reserva de Hoteles que contenga la siguiente información de una reserva
    nombre cliente
    dia de estancia 
    tarifa diaria
    indicar si el cuarto tiene vista al mar 

imprimir el valor de cada variable 
"""

# Definicion de varibles y sistema general 
nombreHuesped = 'Carlos'
diasEstancias = 6
tarifaDia = 20
cuartoVistaAlmar = False

# impresion del ticket 

print("<--- Sistema de Reserva Hoteles --->")
print('Cliente: ',nombreHuesped)
print('Días de Estancia: ',diasEstancias)
print('Tarifa por día: ',tarifaDia)
print('Habitación con vista al mar: ',cuartoVistaAlmar)

# Cambio de valores a las variables 
nombreHuesped = 'Fernando'
diasEstancias = 4
tarifaDia = 30
cuartoVistaAlmar = True

# Impresion de nueva cuenta con datos nuevos

print("<--- Sistema de Reserva Hoteles --->")
print('Cliente: ',nombreHuesped)
print('Días de Estancia: ',diasEstancias)
print('Tarifa por día: ',tarifaDia)
print('Habitación con vista al mar: ',cuartoVistaAlmar)