# Calcular el area y perimetreo de un rectangulo con los datos que de el usuario e imprimir ambos valores
# formula para calcular el area y el primetro 
# Area = base * altura 
# Perimetro = 2* (base + altura)

print("Calculo del area de un Rectangulo")
base = int(input("Ingresa el tamaño de la base: "))
altura = int(input("Ingresa el tamaño de la altura: "))

area = base * altura 
perimetro = 2 * (base+altura)

print(f'La base mide {base}')
print(f'La altura es de: {altura}')

print(f'El area del rectangulo con estos datos es: {area}')
print(f'EL perimetro del rectangulo con las medidas anteriores es: {perimetro}')