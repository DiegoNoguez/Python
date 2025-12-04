# Revision si una variable esta dentro de un rango 

dato=int(input('Proporciona un número: '))

# Revision si esta dentro del rango 
esta_en_rango = 1 <= dato <=10

print(f'La variable esta dentro del rango 1 a 10 {esta_en_rango}')

# Con logica invertida queda asi 

esta_en_rango = not(1 <= dato <=10)

print(f'La variable esta dentro del rango de 1 a 10  {esta_en_rango}')
