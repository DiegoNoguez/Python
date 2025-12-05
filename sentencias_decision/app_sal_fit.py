"""
Creación de una apliacion de consola para simular una apliación fitnes con el 
uso de estructuras condicionales 
"""
# Constantes 
META_PASOS = 10000
CALORIA_PASO = 0.04 # vALOR APROX EN KILOCALORIAS

# SOLCITIDTUD DE DATOS 
nom_usuario = input("Cual es tu nombre: ")
pasos = int(input("Cuantos pasos caminaste hoy: "))

# verificación de si se alcanza la meta 
meta_alcanzada = pasos >= META_PASOS
meta_alcanzada_txt = 'SI' if meta_alcanzada else 'NO'

#Calculo de calorias quemadas
calo_quemadas = pasos * CALORIA_PASO

#Impresion de info 
print(f'<--- Salud Fitnes --->')
print(f'Nombre de usuario: {nom_usuario}')
print(f'Tus pasos fueron: {pasos}')
print(f'Alcanzaste la meta: {meta_alcanzada_txt}')
print(f'Calorias quemadas en kcal: {calo_quemadas}')
print(f'La meta de pasos diarios es : {META_PASOS}')