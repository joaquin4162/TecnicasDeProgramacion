#calcular el area y el perimetro de un triangulo
base = int(input("ingreso de la base"))
altura= int(input("ingreso de la altura"))

perimetro = base * 2 + altura * 2
area = base * altura 

print("perimetro {} - area {}".format(perimetro, area))

#calcular hipotenusa de un rectangulo conociendo sus catetos

import math #libreria que nos da acceso a operaciones matematicas

cateto1 = int(input("Ingreso del 1er Cateto"))
cateto2 = int(input("Ingreso del 2do Cateto"))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2) #la oprecion potencia se escribe **

print("hipotenusa =", hipotenusa)
#•	Escribir un programa que almacene la cadena de caracteres contraseña
# en una variable, pregunte al usuario por la contraseña e imprima por 
#pantalla si la contraseña introducida por el usuario coincide
# con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.


password_valida = "12345"#si esta entre comillas no es un int, es un str

password = input("ingreso del pasword:")

if password == password_valida:
    print("password valida")
else:
    print("password erronea")
    
#En un almacén se rebaja 10% del precio al cliente si compra mas de 20 artículo
#y 5% si compra hasta 20 artículos pero más de 10. 
#Dado el precio unitario de un artículo y la cantidad adquirida, 
#muestre lo que debe pagar el cliente.


#si la cantidad de articulo es >20 tengo 10% de descuento
#si la cantidad de artiuclo es < ó = 20 pero tmb >10 tengo 5% de descuento
#si la cantidad de articulo es < ó = 10 no hay descuento

precio_unitario = int(input("Ingrese el precio unitario:"))
cantidad = int(input("ingrese cantidad:"))

if cantidad > 20:
    descuento = 0.10
if cantidad <= 20 and cantidad > 10: #hay 3 operadores logicos, and(y),or(o),not
    descuento = 0.05                 #and, secumplen las 2 condiciones
if cantidad <= 10:                   #or , es 1 o la otra condicion  
    descuento = 0
    
monto = precio_unitario*cantidad*(1 - descuento)

print("monto a pagar {} con {}% de descuento".format(monto, descuento*100))

#En un almacén se rebaja 10% del precio al cliente si compra mas de 20 artículo
#y 5% si compra hasta 20 artículos pero más de 10. 
#Dado el precio unitario de un artículo y la cantidad adquirida, 
#muestre lo que debe pagar el cliente.


#si la cantidad de articulo es >20 tengo 10% de descuento
#si la cantidad de artiuclo es < ó = 20 pero tmb >10 tengo 5% de descuento
#si la cantidad de articulo es < ó = 10 no hay descuento

precio_unitario = int(input("Ingrese el precio unitario:"))
cantidad = int(input("ingrese cantidad:"))

#if cantidad > 20:
 #   descuento = 0.10
#if cantidad <= 20 and cantidad > 10: #hay 3 operadores logicos, and(y),or(o),not
 #   descuento = 0.05                 #and, secumplen las 2 condiciones
#if cantidad <= 10:                   #or , es 1 o la otra condicion  
 #   descuento = 0

if cantidad >20:
    descuento = 0.10                  #de esta forma no hay que agregar >= o <=
elif cantidad > 10:
    descuento = 0.05           #si tengo un bloque else if, puedo remplazarlo por un elif
elif cantidad > 5:            #codigo origina, else cantidad > 10:
    descuento = 0.02                              # descuento = 0.05
else:
    descuento = 0

monto = precio_unitario*cantidad*(1 - descuento)

print("monto a pagar {} con {}% de descuento".format(monto, descuento*100))