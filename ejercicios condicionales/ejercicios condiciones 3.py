#Realiza un programa que lea dos números por teclado y 
#permita elegir entre 3 opciones en un menú:
#o	Mostrar una suma de los dos números.
#o	Mostrar una resta de los dos números (el primero menos el segundo).
#o	Mostrar una multiplicación de los dos números

#En caso de introducir una opción inválida,
# el programa informará de que no es correcta.

print("Bienvenido")
numero1 = int(input("Ingrese Primer numero: "))
numero2 = int(input("Ingrese Segundo numero: "))

print("elija una opcion")

print("Opcion 1: mostrar una suma de los dos numeros")
print("Opcion 2: mostrar una restra de los dos numeros(el primero menos el segundo)")
print("Opcion 3: mostrar una multiplicacion de los dos numeros")

opcion = int(input("Elija una opcion(numero): "))

if opcion == 1:
    print(numero1 + numero2)
if opcion == 2:
    print(numero1 - numero2)
if opcion ==3:
    print(numero1 * numero2)
if opcion >= 4:
    print("Opcion invalida, solo opciones de 1 al 3")


print("--------------------------")

#Escribir un programa que pregunte al usuario los 3 lados de un triángulo
#y muestre por pantalla que tipo de triángulo es.
print("Bienvenido")

lado1 = int(input("Ingrese lado 1: "))
lado2 = int(input("Ingrese lado 2: "))
lado3 = int(input("Ingrese lado 3: "))

if lado1 == lado2 == lado3:
    print("Tiene 3 lados iguales, es un triangulo equilatero")
if lado1 == lado2 != lado3 or lado1 == lado3 != lado2 or lado2 == lado3 != lado1:
    print("Tiene 2 lados iguales, es un triangulo isosceles")
if lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("Tiene 3 lados diferentes, es un triangulo escaleno")