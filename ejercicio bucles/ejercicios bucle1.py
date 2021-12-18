cont = 0

while cont <= 9:
    print("una palabra")
    cont += 1

#•Escribir un programa que pregunte el nombre del usuario en la consola 
#y un número entero
#e imprima por pantalla en líneas distintas el nombre 
#del usuario tantas veces como el número introducido.

nombre = input("Escriba un nombe: ")
numero = int(input("Escriba un numero: "))
i = 1
while i <= numero:
    i += 1
    print(nombre)
    
#•Leer números enteros positivos de teclado, hasta que el usuario 
#ingrese el 0. Informar cuál fue el mayor número ingresado.

numero1 = int(input("Ingrese numero positivos: "))
n = 0
while numero1 != 0:
    numero1 = int(input("Ingrese numero positivos: "))
    if numero1 > n:
        n = numero1
print("el numero mas alto fue: {}", n)

#•Leer un número entero positivo desde teclado
# e imprimir la suma de los dígitos que lo componen

o = int(input("Ingrese numero positivo:"))
suma = 0
while o != 0:
    digito = o % 10
    suma = suma + digito
    o = o // 10
    print(suma)
    
    
#•Solicitar al usuario que ingrese números enteros positivos y
#, por cada uno, imprimir la suma de los dígitos que lo componen.
# La condición de corte es que se ingrese el número -1. 
# Al finalizar, mostrar cuántos de los números
# ingresados por el usuario fueron números pares.    
    
o = int(input("Ingrese numero positivo: "))
pares = 0
while o > 0:
    if o % 2:
        pares = pares + 1

    suma = 0
    while o != 0:
        digito = o % 10
        suma = suma + digito
        o = o // 10
    print(suma)  
    o = int(input("Ingrese numero positivo: "))
print("numero pares: ", pares)
    
#•Mostrar un menú con tres opciones:
#1- comenzar programa, 
#2- imprimir listado,
#3-finalizar programa.
#A continuación, el usuario debe poder seleccionar una opción (1, 2 ó 3). 
#Si elige una opción incorrecta, informarle del error.
#El menú se debe volver a mostrar luego de ejecutada cada opción,
#permitiendo volver a elegir. Si elige las opciones 1 ó 2 se imprimirá un texto. 
#Si elige la opción 3, se interrumpirá la impresión del menú y el programa finalizará.    
    



while True:
    print("Opcion 1: comenzar a programar")
    print("Opcion 2: Imprimir el listado")
    print("Opcion 3: Finalizar el programa")
    opcion = int(input("Elija una opcion: "))
    if opcion == 1:
        print("Comenzar a programar: ")
    
    elif opcion == 2:
        print("Imprimiendo listado")
    
    elif opcion == 3:
        print("Fin del programa")
        break
    else:
        print("opcion incorrecta, solo validas 1,2,3")

#•Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
#pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta
#.(adicional: cantidad de intentos incorrectos)    

print("Bienvenido")
    
contraseña = input("Ingrese contraseña: ")
contraseña1 = input("Ingrese contraseña nuevamente: ")
intentos = 3
intentosInc = 0
while contraseña != contraseña1:
    print("contraseña incorrecta")
    intentosInc += 1
    intentos -= 1
    print("Numero de intentos restantes: {}".format(intentos))
    if intentos == 0:
        print("saliendo del programa")
        break
    contraseña1 = input("Ingrese contraseña nuevamente: ")
       
print("numero de intentos incorrectos: {}".format(intentosInc))   

#•Escribir un programa que permita al usuario ingresar un conjunto de notas, 
#preguntando a cada paso si desea ingresar mas notas. Luego imprimir el promedio de notas.

nota = int(input("Ingrese nota: "))
cantidad = 0
total = 0
while nota != 0:
    cantidad += 1
    total += nota
    si_no = input("Ingresar mas notas?(si/no): ")
    
    if si_no == "si":
        nota = int(input("Ingrese nota: "))
    if si_no == "no":
        print("Saliendo")
        break
print("Promedio de notas: {}".format(total/cantidad))       

        