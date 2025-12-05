"""
Docstring for sentencias_decision.reserv_hotel
Ejecuantdo mediante consola 
    Solicitar los datos al usuario 
        Nombre de cliente 
        dias de estadia 
        cuarto con vista al mar      
"""
# Definicion de constantes 
CUARTO_VISTA_MAR = 190.50
CUARTO_SIN_VISTA_MAR = 150.50

print(f' SIstema de reservación ')

# solicitud de datos 
cliente = input("Ingresa tu nombre: ").strip()
dias_estadia = int(input("Cuantos días sera tu estancia: "))
vista_mar = input("Quieres vista al mar (si/no): ").strip().lower()

# desarollo de logica 
con_vista  = 'si' if vista_mar == 'si' else 'No'
if vista_mar == 'si':
    costo_final = dias_estadia * CUARTO_VISTA_MAR
    preciox_dia = CUARTO_VISTA_MAR
else:
    costo_final = dias_estadia * CUARTO_SIN_VISTA_MAR
    preciox_dia = CUARTO_SIN_VISTA_MAR

# IMPRESION FINAL 
print(" ---Costo final de la reservacion--- ")
print(f'Los días de estadia son: {dias_estadia}')
print(f'La habitación tiene vista al mar: {vista_mar}')
print(f'El precio por día es de: {preciox_dia}')
print(f'EL total a pagar es: {costo_final}')
