# Ejercicio de calculadora con opciones de suma, resta, multipliacacion, division 
# el programa debe de msotrar un menu  y solicitar los valores con los cuales va 
# a operar.
print("<---- CALCULADORA EN PYTHON ---->")
salir = False
while not salir:
    print(''' Opciones a relaizar:
          1).- Suma
          2).- Resta
          3).- Multipliación
          4).- División
          5).- Salir''')
    opcion = int(input("Ingresa la opción a realizar: "))

    if opcion == 1:
        num1 = int(input("Ingresa un número: "))
        num2 = int(input("Ingresa el segundo número: "))
        suma = num1 + num2
        print(f'EL resultado de la operacion con los numeros dados es: {suma}')
    elif opcion == 2:
        num1 = int(input("Ingresa un número: "))
        num2 = int(input("Ingresa el segundo número: "))
        resta = num1 - num2
        print(f'El resultado de la operación es: {resta}')
    elif opcion == 3:
        num1 = int(input("Ingresa un número: "))
        num2 = int(input("Ingresa el segundo número: "))
        multi = num1 * num2
        print(f'El resultado de la operación es: {multi}')
    elif opcion == 4:
        num1 = int(input("Ingresa un número: "))
        num2 = int(input("Ingresa el segundo número: "))
        if num2 > 0 :
            divid = num1/num2
            print(f'El resultado de la operación es: {divid}')
        else:
            print(f'Division por cero no existe.') 
    elif opcion == 5:
        print("Adios, saliendo del sistema.")
        salir = True
    else :
        print(f'Opcion no valida ni registrada: {opcion}')
    print("\n")
