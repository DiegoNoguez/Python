""" SISTEMA DE EMPLEADO 
    Crear un programa para solicitar la informacion de un 
    empkeado, introduciendo  los daros por consola 
        Nombre empleado 
        edad del empleado 
        Slario del empleado 
        Es jefe de departamento 
    """

# Definición de variables
dis = "-"

# Desarollo de la logica
disRep = dis * 3



# Impresion de los datos
print(f'{disRep} Sistema de Empelados {disRep}')
nombreEmpleado = input("Nombre empleado: ")
edadEmpleado = int(input("Edad del empleado; "))
salarioEmpleado = int(input("Salario del empleado: "))
esJefe = input("Es jefe de depertamento (si/np) ")
esJefe  = esJefe.lower() == 'si'

# Impresion de los valores Empleado
print('\nDatos del empleado')
print(f'Nombre: {nombreEmpleado}')
print(f'Edad: {edadEmpleado}')
print(f'Salario: {salarioEmpleado:.2f}')
print(f'Es jefe de Departamento: {esJefe}')