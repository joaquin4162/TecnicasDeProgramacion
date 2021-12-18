#Diccionarios - 'key': value
#es una coleccion no ordenada de objetos, es por eso que para indentificar un valor(value)
#cualquiera dentro de este, necesitamos refenciarlo mediante una clave (key)

#para crear un diccionarios se emplean las llaves {}, y sus pares clave-valor se separan por comas
#a su vez, intercalamos la clave del valor con 2 puntos


dic = {'nombre' : 'joaquin', "apellido" : "sosa", "edad" : 23, 34.4 : None}

listas = ["joaquin", "sosa", 23]



print(dic)

print(type(dic)) #metodo type, nos devuelve que tipo es

#tmb podemos usar len
print(len(dic)) #el elemento es key:value, cuenta como 1 solo

#si quiero imprimir cada elemento tenemos que poner la key, no el sub indice

print(dic["apellido"]) #lee los valores de los diccionarios, si esta mal esctiro o no existe tira error

#otra forma de acceder al diccionario
#metodo get

print(dic.get("edad"))#si el elemento esta mal escrito o no existe, devuelve "none"





"los diccionarios se peuden modificar, como las litas"
"se modifican los valores, no las key"

dic["edad"] = 25
print(dic)

#agregar datos a las listas

dic["dni"] = 41111111

print(dic)

dic["profesion"] = "Nada"

print(dic)

#como eliminar datos de un dic
#pop

dic.pop(34.4)

print(dic)

#popitem, elimina el ultimo par key:value

#elemento del

del dic["edad"]
print(dic)

#elemento clear, elimina todos los elementos del diccionario

dic.clear()
print(dic)


