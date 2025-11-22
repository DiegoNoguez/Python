""" Generador de email con nuevas mejoras
    Crea un programa para generar un email a partir de los
    siguintes datos
    Nombre: Diego Noguez
    Empresa : Global Mentoring 
    Dominio: com.mx 

    Reultado final
    email: nombreusuario@empresa.dominio
    Los datos mostrados son de ejemplo y solo 
    se usa para reforzar el ejercicio de funciones con cadenas o Strings 
    Con entrada de datos por consola 
    """
# Inicio del programa 
print(f'<----- Sistema Generador de Email ----->')
nombreUsurio = input("Ingresa tus nombre o nombres: ")
apellido = input("Ingresa tus Apellidos: ")
nombreEmpresa = " SpringyTec Solutions "
extensionDominio  = " .com.mx "

# Generacion de la logica
nombreCompleto = nombreUsurio + apellido
usuario = nombreCompleto.strip().lower().replace(' ','.') 
nombreEmpresa = nombreEmpresa.strip().lower().replace(' ','')
dominio = extensionDominio.strip()

# Impresion de lso datos 
print(f'\nNombre de usuario: {nombreCompleto}')
print(f'Nombre de la emprea: {nombreEmpresa}')
print(f'Estensión o dominio: {dominio}')
print(f'Corrreo Final:{usuario}@{nombreEmpresa}{dominio} ')