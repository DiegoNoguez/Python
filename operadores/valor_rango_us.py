# Verificar si un valor es dentro del reango con el uso de constantes
VAL_MIN = 0
VAL_MAX = 20

print("Verificadador si el valor esta dentro del rango")
valor = int(input("Ingresa un número: "))
eval_rango = valor >= VAL_MIN and valor <=VAL_MAX
print(f'EL valor dado esta dentro del rango de {VAL_MIN} y de {VAL_MAX}: {eval_rango}')