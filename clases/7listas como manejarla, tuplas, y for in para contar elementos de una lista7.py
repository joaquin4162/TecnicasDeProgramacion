#listas, alterables []
numero = [1, 3 ,5 ,7 ,9]#corchete para definir la lsita
mi_lista = ["A", "C", "F"]
print(numero)#imprime la lista completa
print(mi_lista)
print(numero[0])#entre [] para acceder al dato del subindice que indiquemos
print(mi_lista[2])
print(numero[3])
print(len(mi_lista))#len devuelve un entero que respresenta la cantidad de elementos de la lista 
largo = len(numero)
print(largo)

#concepto de modif de lista

mi_lista[2] = "D" #elegimos la posicion y ponemos el nuevo dato
print(mi_lista)

mi_lista.append("E")#agregamos elementos dinamicamente a la lista, pero al final
print(mi_lista)
print(len(mi_lista))

#metodo insert

mi_lista.insert(1, "B")#inserta el elemneto en la posicion que le indica, y desplaza el resto
print(mi_lista)


#remove, elimina el elemento indicado

mi_lista.remove("E")
print(mi_lista)

#para eliminar algo en un posicion

del mi_lista[3]
print(mi_lista)

#metodo pop, sirve para eliminar el ultimo elemento de la lista

mi_lista.pop()
print(mi_lista)

#ordenar lista sort(), reverse() si y solo si mi lista es del mismo tipo, es lo ideal
print(numero)
numero.reverse()
print(numero)
mi_lista.reverse()
print(mi_lista)

numero.sort()
print(numero)

#tupla, inalterable ()
#tipo de dato de solo lectura
una_tupla = (1, 2, 3, 4 ,5) # si intento agragar, elimiar o mover un elemento tira error

print(una_tupla)

#encontrar valores en la lista o en la tupla, se puede conbinar con if, se usa in o not in

if 5 in una_tupla:
    print(" 5 esta en la tupla")
else:
    print("no lo encontro")
 
if 9 not in una_tupla:
    print(" 9 no esta en la tupla")
else:
    print("lo encontro")
    
    
    
    
    
#iterar una lista o un diccionario #elementos iterables listas ,tuplas y diccionarios
#iterable, que tiene la capacidad de repetirse
#For - in(), bucle que repite el bloque de instrucciones un numero predet de veces


numero = [1, 3 ,5 ,7 ,9]
mi_lista = ["A", "C", "F"]
        
print(numero)

largo = len(numero)
i = 0
while i < largo:
    print(numero[i])
    i = i + 1
    
print("Imprimiendo con for()")
for item in numero:
    print("una pasada")
    print(item)


