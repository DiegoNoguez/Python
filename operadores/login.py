# Sistema estilo login pero en consola 
usuario_bien = "Adrew"
contra = "1234"
guion = "-"
guion = guion*4
print(f'{guion} Inicia sesion con las credenciales correctas {guion}')

user = input("Digita tu usuario: ")
password =input("Ingresa tu contraseña: ")
correcto = (user.strip() == usuario_bien and password.strip() == contra)
print(f'Los datos ingresados son {correcto}')
