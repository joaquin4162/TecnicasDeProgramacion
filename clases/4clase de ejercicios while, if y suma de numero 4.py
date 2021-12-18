#Escribir un programa que pregunte el nombre del usuario en la consola
#y un numero entero e imporima por pantalla en lineas distintas
#el nombre del usuario tantas veces como el n° introducido

nombre = input("Ingrese el nombre: ")
cantidad = int(input("Ingrese cantidad: "))

#validar que ingrese numeros positivos
while cantidad < 0:
    print("Ingreso no valido, solo se aceptan numeros positivos")
    cantidad = int(input("Ingrese cantidad: "))
i = 0
while i<cantidad:
    print(nombre)
    i = i + 1

print("----------------------------------")

#leer numero enteros positivos de teclado, hasta que el usuario ingrese el 0
#informar cual fue el mayor numero ingresado

mayor = -1
numero = int(input("Ingrese un numero: "))
menor = 9999999999999999999
i = 0
while numero > 0:
    if numero > mayor:
        mayor = numero
    if numero < menor:
        menor = numero
        
    numero = int(input("Ingrese un numero: "))
    
print("Mayor numero ingresado: {} - Menor numero: {}".format(mayor, menor))

print("----------------------------------")


#lo hizo el culiado de anderson
numero=int(input('ingrese numeros para hallar su máx, ingrese 0 para terminar\n'))
maximo=numero
minimo=numero

while numero!=0:
	if numero>maximo:
		maximo=numero
	if numero<minimo:
		minimo=numero
	numero=int(input('ingrese el siguiente numero\n'))

print('valor maximo',maximo)
print('valor minimo',minimo)

print("----------------------------------")

#leer un numero entero positivo desde el teclado e imprimir
#la suma de los digitos que lo componen

numero = int(input("Ingrese un numero positivo: "))
cantidad_pares = 0

while numero > 0:
    
    if numero % 2 == 0:
        cantidad_pares = cantidad_pares + 1
        
    suma = 0
    while (numero != 0):
            digito = numero % 10
            suma = suma + digito
            numero = numero // 10
    print("suma", suma)
    numero = int(input("Ingrese un numero positivo: "))

    
print("cantidad numero pares: ", cantidad_pares)
    