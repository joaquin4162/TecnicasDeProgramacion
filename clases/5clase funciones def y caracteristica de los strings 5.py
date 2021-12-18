# y = x2 + 4
#def palabra definida para funcion( se utilizan para reuitilizar codigos)
def operacion(x):
    print("Estoy en la funcion")
#    

    res = x * x + 4
    return res    #retorno
    
x = int(input("ingrese x: "))

resultado = operacion(x)

print("el resultado es: {}".format(resultado))

def operacion(a):
    print("Estoy en la funcion")
    res = a * a + 4
    return res    #retorno
    
x = int(input("ingrese x: "))

resultado = operacion(x)

print("el resultado es: {}".format(resultado))

p = int(input("ingrese p: "))

resultado = operacion(x)

print("el resultado es: {}".format(resultado))


print("........................")

def operacion(a):
    print("estoy en la funcion")
    res = a * a + 4
    
    return res

x = int(input("ingrese x: "))

resultado = operacion(x)

print("el resultado es: {}".format(resultado))

print("............................")
#en este caso la funcion muere ahi, no retorna nada
def operacion(a):
    print("estoy en la funcion")
    res = a * a + 4
    print("el resultado es: {}".format(res))
    return

x = int(input("ingrese x: "))

operacion(x)

print("--------------")


def calcular(p, d):
    print("estoy en la funcion")
    descuento = (d / 100) * p
    pagar = p - descuento
    
    return pagar

precio = int(input("ingrese precio: "))
desc = int(input("ingrese descuneto (en %): "))

resultado = calcular(precio, desc)
print("a pagar: {}".format(resultado))

precio = int(input("ingrese otro precio: "))
desc = int(input("ingrese descuneto (en %): "))

resultado = calcular(precio, desc)
print("a pagar: {}".format(resultado))

print("-------------------------")
print("Bienvenido")
def menu():
    print("Ingrese 1 para ver su saldo")
    print("Ingrese 2 para transferir")
    print("Ingrese 3 para salir")
    
    opcion = int(input("opcion: "))
    
    return opcion
while True:
    opcion = menu()

    if opcion == 1:
        print("su saldo es 0$")
    elif opcion == 2:
        print("usted esta transfiriendo")
    elif opcion == 3:
        print("chau")
        break
    else:
        print("usted ingreso cualaquier cosa")
        break
print("saliendo")



print(":...........................")


frase = "hola mundo desde python"

print(frase)
print(frase[0])
print(frase[5])#entre corchetes va el espacio del caracter
print(frase[-1])# con los negativos va de atras para adelante
print(frase[-2])


# funcion len, acepta un argunmento y retorna algo
#muestra y mide el largo del string

largo = len(frase)#sirve para ejercicios de manejos de caracteres

print(largo)

#print(frase[30]) esto nos da error por que el string esta fuera de rango

#slicing, capacidad de la cadena que devuelve un subconjunto o sub cadena
#utilizando 2 indices

print(frase[0:4])#el primer numero indica el incio y el segundo el final

print(frase[2:8])

#inmutabilidad las cadenas no se pueden modificar
#frase[0] = "H"
#print(frase) ESTO DA ERROR

frase2 = frase[1:]
print(frase2)
nuevafrase = "H" + frase2
print(nuevafrase)#en este caso concatenamos


print(frase.capitalize())#pone en mayuscula la primera
print(frase.upper())

print(frase.count(" "))#conto los espacion

#cuantas palabras tiene frase?
cantidad = frase.count(" ")
print("Cantidad de palabras: {}".format(cantidad + 1))
















