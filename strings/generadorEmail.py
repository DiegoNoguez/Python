# Ejercicio de generar correos solo usando manejo de cadenas
""" Crea un programa para generar un email a partir de los
    siguintes datos
    Nombre: Diego Noguez
    Empresa : Global Mentoring 
    Dominio: com.mx 

    Reultado final
    email: nombreusuario@empresa.dominio
    """

#Definicion de varibales 
nombreUs="Diego Arturo Noguez Lopez"
empresa = "Global Mentoring"
dominioExtends = ".com.mx"
guiones = '-'

# Desarollo de la logica
# Normalizacion de nombre de usuario y de empresa
# Nombre de usuario
nombreMinus= nombreUs.lower().replace(' ','.')
# Dominio de email
empresaNom = empresa.lower().replace(' ', '.')
dominioNom=empresaNom + dominioExtends
# Repeticion de guiones
repetir = guiones * 4

# impresion 
print(f'{repetir} Generador de Email {repetir}')
print(f'Nombre de Usuario: {nombreUs}')
print(f'Nombre normalizado: {nombreMinus}')
print()
print(f'Nombre de la empresa: {empresa}')
print(f'Extension del dominio: {dominioExtends}')
print(f'Dominio de eamil: @{dominioNom}')
print()
print(f'Email final generado: {nombreMinus}@{dominioNom}')
