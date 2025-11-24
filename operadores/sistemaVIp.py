# SItema de descuento 
print('<--- Sistema de Descuentos Vip --->')

NO_PRODUCTOS_DESCUENTO = 10
cantidad_productos = int(input("Cuantos productos compraste hoy: "))
tiene_membresia = input("Tienes la mebresia de la tienda: ")

tiene_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTO
                   and tiene_membresia.strip().lower() == 'si')

print(f'TInes acceso al descuento VIP: {tiene_descuento}')