"""
    Crear un sistema que ofrezca descuentos dependiendo del monto de la compra, o si es miembro de la tienda 
    Se debe de revisar las siguientes condiciones:
        Si ha comprado mas de 1000 y es miembro --> Descuento de 10%
        Si solo es miembro de la tienda descuento del 5
        Si no es miembro ni compro mas de 1000 descuento del 0 

"""

print("Creacion de pago tienda en linea")
compra =float(input("Cual fue tu monto de compra: "))
miembro = input("Eres mienbro de la tienda s/n: ").strip()
print(f'El monto de la compra es: {compra}')
if compra >= 1000 and miembro == "s".strip():
    descuento = compra * 0.10
    montoFinal = compra - descuento
    print(f'Tienes el siguiente descuento: {descuento}')
    print(f'El monto final es de: {montoFinal}')
elif miembro == "s":
    descuento = compra * 0.05
    montoFinal = compra - descuento
    print(f'Tienes el siguiente descuento: {descuento}')
    print(f'El monto final es de: {montoFinal}')
else: 
    montoFinal = compra
    print(f'El monto final es de: {montoFinal}')



