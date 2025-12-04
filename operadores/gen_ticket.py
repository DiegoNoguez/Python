# Generador ticket 
guion = '-'
guion = guion*3
print(f'{guion} Tciket venta {guion}')

# Precio del producto 
soda= float(input('Ingresa el precio de la soda:'))
pan = float(input('Ingrea el precio del pan:'))

# Calculo del subtotoal sin impuestos 
subtotal = soda+pan
print(f'El subtotal es {subtotal}')
impuesto = subtotal*0.16
total = impuesto +subtotal
print(f'El total a pagar ya con impuestos es {total}')