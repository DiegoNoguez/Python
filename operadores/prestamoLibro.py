# Es un ejemplo de como usar el operador logico de or 
print('<--- SIstema Prestamo Libros --->')

DISTANCIA_PERMITIDA =3
tienecredencial = input("Cuentas con credencial de estudiante: ")
distanciaBiblio = int(input("Cuantos km vives de la biblioteca: "))

pretamoLibro = (tienecredencial.strip().lower() == 'si'
                or distanciaBiblio <= DISTANCIA_PERMITIDA)

print(f'Eres valido para tener un libro prestado: {pretamoLibro}')
