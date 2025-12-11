# SUma acumulativa usando el ciclo while 

print("Suma acumulativa")

MAXIMO = 6
numero = 1
acumulador_suma = 0

# Desarrollo de la iteracion en ciclo while
while numero <= MAXIMO:
    print(f'Los datos que se estan sumando son {numero} + {acumulador_suma}')
    acumulador_suma += numero
    numero += 1
    print(f'Suma parcial de los valores: {acumulador_suma}')
print(f'EL resultado de la suma acumulada: {acumulador_suma}')