# Usando sentencias de decision para saber si un numero es positivo o negativo 

num = int(input("Ingresa un número: "))
if num>0:
    print(f'EL numero dado {num} es positivo')
elif num<0:
    print("El numero es negativo")
else:
    print("El numero es 0")