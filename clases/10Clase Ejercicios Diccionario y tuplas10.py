
#escribir un programa que procese cadenas de texto ingresados por el usuario
#la lectura finaliza cuando se haya ingresado una cadena vacia
#al finalizar, informar la cantidad total de ocurrencias de cada palabra
#en todos las cadenas ingresadas, ejemplo: "que" = 2. "tal" =1
#"como se podrian informar ademas las ocurrencias de espacios"



contador_palabra = {}
cantidad_De_espacios = 0

while True:
    cadena = input("ingrese una frase: ")
    if cadena == '':
        break
    lista_palabras = cadena.split()
    
    print(lista_palabras)
    for palabra in lista_palabras:
        if palabra not in contador_palabra:
            contador_palabra[palabra] = 1
        else:
            contador_palabra[palabra] += 1
            
    cantidad_De_espacios += cadena.count(" ")
    
print(contador_palabra)
print("cantidad de espacion contados: ",cantidad_De_espacios)



print("_______________________")

#Escribir una funcion que reciba un alista de tulpas(pais,ciudad)
#y que devuelva un diccionario en donde las claves sean los paises, y los valores una lista con las ciudades

ciudadesPaises = [("Argentina", "Cordoba"),("Argentina", "Corriente"),("Chile","Santiago")]

def ciudadesPorPais(lista):
    dict = {}
    for pais, ciudad in lista:
        if pais not in dict:
            dict[pais] = [ciudad]
        else:
            dict[pais].append(ciudad)
        
    return dict
        
dictCiudades = ciudadesPorPais(ciudadesPaises)    

print(dictCiudades)

# obtener ciudades encontradas en un pais

print(dictCiudades["Argentina"])

for ciudad in dictCiudades["Argentina"]:
    print(ciudad)
    
#Buscar si esxiste un pais
print(dictCiudades.keys())#devuleve las key
if "Argentina" in dictCiudades.keys(): #aca bysca en el diccionario, y ve si existe argentina
    print("Se encontro el pais")

if "Cordoba" in dictCiudades: #aca estamos viendo el valor de "argentina" entonces no devuelve nada
    print("existe la ciudad")

print(dictCiudades.values())

for item in dictCiudades.values(): #iteramos en los valores del diccionario
    if "Cordoba" in item:
        print("Existe la ciudad")