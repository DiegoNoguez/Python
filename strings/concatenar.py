# Manera de como concatenar cadenas en Python 

nombre = 'Ivan'
saludo = 'Hola'
despedida = 'adios'

print(saludo)

fraseCompleta = saludo + nombre
print(saludo+nombre)

# Si se intenta concatenaer con numeros python retorna errores 
# la forma correcta de hacerlo es 
edad = 25 
#IMpresion con catenación
print(str(nombre)+edad) # o usando comas.

# Otra forma de hacerlo es con f-string manera moderna y mas recomendada
print(f'Hola {nombre}, tienes {edad} años')

# USando el metodo format
mensaje = "{}, {}, tienes {} años".format(saludo, nombre, edad)


# Ejemplo de aplicaion de lo anterior

# 1.- Usando el operador +
apellido = 'Galvan'
nombreCompleto = nombre + '' + apellido
print(nombreCompleto, 'Usando el operador de +')
