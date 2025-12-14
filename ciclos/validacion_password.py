# CREACION Y VALIDACION DEL PASSWORD

print('Creacion y validacdion del password')

contra = input('Ingresa un password(debe de contener al menos 6 caracteres): ')

while len(contra):
    print('El password no cumple con los requisitos. Debe tener al menos 6 caracterees')
    contra = input('Ingresa una nuevo valor de password: ')
else:
    print('El valor de password es valido.')