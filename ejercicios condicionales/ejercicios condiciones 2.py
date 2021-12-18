numero = int(input("Inserte un numero entero: "))

if numero < 0:
    print("valor absoluto: {},{}".format(numero * -1, numero))
else:
    print("valor absoluto: {}".format(numero))


print("--------------------------------------------")

numero1 = int(input("Ingrese primer numero: "))
numero2 = int(input("Ingrese segundo numero: "))

if numero1 == numero2:
    print("{} y {} son iguales".format(numero1, numero2))
if numero1 != numero2:
    print("{} y {} son diferentes".format(numero1, numero2))
if numero1 > numero2:
    print("{} es mayor que {}".format(numero1, numero2))
if numero1 < numero2:
    print("{} es menor que {}".format(numero1, numero2))
    
print("--------------------------------------------")

#debe ser divisible por 4 y no debe ser divisible por 100
#excepto que también sea divisible por 400

año = int(input("Ingrese un año de 4 digitos: "))

if año % 4 != 0:
    print("No es un año bisiesto")
elif año % 4 == 0 and año % 100 != 0:
    print("Es un año bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 != 0:
    print("No es un año bisiesto")
elif año % 4 == 0 and año % 100 == 0 and año % 400 == 0:
    print("Es un año bisiesto")
    #analizarlo bien
    
print("--------------------------------------------")

interruptor1 = int(input("Elegir entre 1 y 0: "))
interruptor2 = int(input("Elegir entre 1 y 0: "))
interruptor3 = int(input("Elegir entre 1 y 0: "))

cerrado = 1
abierto = 0

if interruptor1 == cerrado:
    print("el interruptor esta cerrado")
else:
    print("el interruptor esta abierto")
if interruptor2 == cerrado:
    print("el interruptor esta cerrado")
else:
    print("el interruptor esta abierto")
if interruptor3 == cerrado:
    print("el interruptor esta cerrado")
else:
    print("el interruptor esta abierto")
    
if interruptor1 == cerrado and interruptor2 == cerrado or interruptor1 == cerrado and interruptor3 == cerrado or interruptor2 == cerrado and interruptor3 == cerrado:
    print("el circuito esta cerrado")
else:
    print("el circuito esta abierto")
    
#pude recortar un poco el codigo
interruptor1 = int(input("Elegir entre 1 y 0: "))
interruptor2 = int(input("Elegir entre 1 y 0: "))
interruptor3 = int(input("Elegir entre 1 y 0: "))

cerrado = 1
abierto = 0

if interruptor1 == cerrado:
    print("el interruptor esta cerrado")
else:
    print("el interruptor esta abierto")
if interruptor2 == cerrado:
    print("el interruptor esta cerrado")
else:
    print("el interruptor esta abierto")
if interruptor3 == cerrado:
    print("el interruptor esta cerrado")
else:
    print("el interruptor esta abierto")
    
if interruptor1 == cerrado == interruptor2 or interruptor1 == cerrado == interruptor3 or interruptor2 == cerrado == interruptor3:
    print("el circuito esta cerrado")
else:
    print("el circuito esta abierto")
    
    
print("-----------------------------------")

#grados Fahrenheit a grados Celsius. Recuerde la fórmula: F = 9/5 C + 32

F = int(input("Ingrese grados Fahrenheit: "))

c = ((F - 32)*5)/9

print("Grados Celcius: {}".format(c))
    
    
    
    
    
    
    
    
    
    
    
    
    
    

