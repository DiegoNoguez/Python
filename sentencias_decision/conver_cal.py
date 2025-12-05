# Conversor de calificaciones 
"""Docstring for sentencias_decision.conver_cal

    Crear un programa para convertir calificaciones numericas del 0-10 
    a una letra ( del F-A)
"""

print(" Conversor de calificaciones \nNumericas a Letras")
cal= int(input("Ingresa tu calificacion del 0-10: "))

if cal <= 10 and cal >=9:
    print("La calificacion es de: A")
elif cal < 9 and cal >=8:
    print("La calificacion es de: B")
elif cal >=7 and  cal < 8:
    print("La calificacion es de: C")
elif cal >= 6 and cal < 7:
    print("La calificacion es de: D")
elif cal >=0 and cal <6:
    print("La calificacion es de: F")
else:
    print("Valor desconocido")