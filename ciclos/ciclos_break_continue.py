# break y continue en ciclos 

print("  Break y continue   ")
# ejemplo con break 
print("Usando la palabra breal ")
for numero in range(1,11):
    if numero % 2 ==0:
        print(numero)
        break   # Se sale del ciclo de forma rapida es decir se rompe el ciclo 

# Ejemplo con continue 
print("Usando la palabra continue ")
for numero in range(1,11):
    if numero % 2 == 1:
        continue  # Continuea con la iteracion del ciclo 
    print(numero) # imprime solo los numeros pares 