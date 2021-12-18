#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
print("Bienvenido")
edad = int(input("Ingrese su edad:"))
 
print("Usted tiene: {} años".format(edad))
if edad > 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")
    print("Saliendo del programa")

#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

numero = int(input("Ingrese un numero:"))

if numero % 2 == 0:
    print("el numero es par")
else:
    print("el numero es inpar")

#igualar contraseña    
contraseña_valida = '4162'
contraseña = input("Ingrese contraseña:")

if contraseña == contraseña_valida:
    print("Contraseña valida")
else:
    print("Contraseña invalida")
    