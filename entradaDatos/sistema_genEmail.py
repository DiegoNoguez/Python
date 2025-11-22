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
    """
# Inicio del programa 
print(f'<----- Sistema Generador de Email ----->')
nombreUsurio = input("Ingresa tus nombre o nombres: ")
apellido = input("Ingresa tus Apellidos: ")
nombreEmpresa = " SpringyTec SOlutions "
extensionDominio  = " .com.mx "

# Generacion de la logica
nombreCompleto = nombreUsurio + apellido
nombreCompleto = nombreCompleto.strip().lower().replace(' ','.') 

# Impresion de lso datos 
print(f'\nNombre de usuario: {nombreCompleto}')
print(f'Nombre de la emprea: ')
print(f'Corrreo Final: ')