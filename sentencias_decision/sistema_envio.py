# SISTEMA DE ENVIOS

# CONSTANTES
COSTO_NACIONAL = 10
COSTO_INTERNACIONAL = 20

print("--- Sistema de Envios---")
destino = input("Tu destino es nacional o internacional (n/i): ")
peso = int(input("Cuantos kilos pesa el paquete: "))

# Logica 
if destino == 'n':
    costo_final = peso * COSTO_NACIONAL
else:
    costo_final = peso * COSTO_INTERNACIONAL

# impresion final 
print("---COSTO FINAL DE ENVIO---")
print(f'EL destino es: {destino}')
print(f'El envio tiene un peso de: {peso} kg')
print(F'Costo final de envio es: {costo_final}')