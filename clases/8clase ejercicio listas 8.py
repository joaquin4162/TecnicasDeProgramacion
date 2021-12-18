#escribir una funcion que dado un string, retorne la long de la palabra mas larga
#se considera las palabras estan separadas por uno o mas espacios
#tambien podrias haber espacios al princpicio o al final del sting pasado por parametro
def largoPalabraMasLarga(frase):
    indice = 0
    longitud = 0
    maxima_longitud = 0
    if len(frase) == 0:
        return 0
    while indice < len(frase):
        if frase[indice] != " ":
            longitud += 1
        if frase[indice] == " " or indice == len(frase)-1:
            if longitud > maxima_longitud:
                maxima_longitud = longitud
            longitud = 0
        indice = indice + 1
    return maxima_longitud

#una forma mas corta con listas
def palabraMasLarga(frase):
   palabras = frase.split()
   
   largo = 0
   palabra_larga = ""
   for palabra in palabras:
       if len(palabra) > largo:
           largo = len(palabra)
           palabra_larga = palabra
      
   return largo, palabra_larga


frase = "Hola mundo programando desde python"
print(largoPalabraMasLarga(frase))

print(frase.split())#transforma la frase en una lista

largo, palabra = palabraMasLarga(frase)
print("Largo palabra: ",largo)#es como un format
print("palabra: ", palabra)

print("__________________________")

#A)Solicitar al usuario que ingrese numeros, los cuales se guardan en una lista
#finalizar el ingresar el 0, el cual no se debe guardar
#B)solicitar al usiario que ingrese un numero y, si esta en la lista
#eliminar su prumera ocrrencia, mostrar un msj si no es posible eliminar
#C)recorrer la lista para imprimir la sumatoria de todos los elementos
#D)solicitar al usuario otro num, y crear una lista con los elemnetos de la lista original
#que sean menores que el numero dado, imprimir la nueva lista, iterando por ella


#A)
numero = int(input("Ingrese numero: "))
numeros = [] #esto indica que es tipo lista y esta vacio
while numero != 0:
    numeros.append(numero)
    numero = int(input("Ingrese numero: "))
    
print(numeros)

#B)

numero_a_eliminar = int(input("Ingrese numero a eliminar: "))

if numero_a_eliminar in numeros:
    
    numeros.remove(numero_a_eliminar)
else:
    print("Numero no encontrado")
print(numeros)

#C)
total = 0
for numero in numeros: #usamos para iterar(cambiar o manipular)
    total = total + numero
    
print("sumatoria de los numeros: ", total)

#D)

numeroLimite = int(input("Ingrese numero limite: "))
numerosMenores = []
for numero in numeros:
    if numero < numeroLimite:
        numerosMenores.append(numero)
        
print(numerosMenores)




print("_________________")

#ingresar notas de los alumnos en una lista, el fin de ingreso de nota es nota = 0
#calcular e informar
#A) promedio nota
#B) nota mas alta
#C) listado ordenado de nota(< a >)
#D) listado de nomta que superen el promedio de notas


def calcularPromedio(notas):
    sumaNotas = 0 #adento del def, por que despues no se usa
    for nota in notas:
        sumaNotas = sumaNotas + nota
    
    promedio = sumaNotas / len(notas)
    
    return promedio

def calcularNotaMaxima(notas):
    notaMasAlta = 0
    for nota in notas:
        if nota > notaMasAlta:
            notaMasAlta = nota
    return notaMasAlta

notas = []
while True: #bucle infinito
    nota = int(input("Ingrese nota(entre 0 y 10): "))
    
    if nota == 0: #si nota = 0 
        break #  se cumple el if y se rompe el bucle
        
    notas.append(nota)
print(notas)

#A) 

promedio = calcularPromedio(notas)

print(promedio)

#B)

notaMasAlta = calcularNotaMaxima(notas)

print(notaMasAlta)

#C)
#para ordenar usamos sort de menor a mayor 

notasOrdenadas = sorted(notas) # ordena la lista sin modificarla
print("notas", notas)
print("notas ordenadas", notasOrdenadas)

#D)
mejoresNotas= []
for nota in notas:
    if nota > promedio:
        mejoresNotas.append(nota)
print("mejores notas: ", mejoresNotas)
    




