listado = [ ( "juan", "perez", 1000),
           ("pedro","sanchez", 2000),
           ("maria", "gonzalez", 3000) ]
suma = 0
cantidad = 0
for registro in listado:
    suma = suma + registro[2]
    cantidad = cantidad + 1
    
promedio = suma / cantidad
print (promedio)


listado2 = []
for registro in listado:
    if registro[2] < promedio:
        listado2.append(registro)
        
print(listado2)
