# GENERACION DE UN VALPR ALEATORIO 
from random import randint
numeroAdvini = randint(1,50)

print("<--- ADIVINA EL NÚMERO --->")
num = 0
contador = 0
while contador <=15 and num != numeroAdvini:
    num = int(input("Adivina el número de 1-50: "))
    if num < numeroAdvini:
        print("El numero es mayor")
    elif num > numeroAdvini:
        print("El numero es menor")
    contador +=1

print(f'Felicidades adivinaste el numero es: {numeroAdvini}\n')
print(f'Lo lograste con un total de {contador} intentos')