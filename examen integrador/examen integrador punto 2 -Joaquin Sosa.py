#import csv

dato = {
        "nro_part": "",
        "nombre": "",
        "apellido": "",
        "edad": "",
        "sexo": "",
        "disparo1": "",
        "disparo2": "",
        "mejor_disparo": ""
        }

participantes = []
cant_part = 0
cant_mujeres = 0
prom_edadhom = 0
prom_mejordisp = 0
prom_disparos = 0
while True:
    
    
    nro_part = int(input("Nro de participante: "))
    if nro_part == 999:
        break
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo (f/m): ")
    disparo1 = int(input("Disparo1: "))
    disparo2 = int(input("Disparo2: "))
    
    cant_part = cant_part + 1
    
    if disparo1 < disparo2:
        mejor_disparo = disparo1
    if disparo2 < disparo1:
        mejor_disparo = disparo2
        
    dato = {
        "nro_part": "",
        "nombre": "",
        "apellido": "",
        "edad": "",
        "sexo": "",
        "disparo1": "",
        "disparo2": "",
        "mejor_disparo": ""
        }


    dato["nro_part"] = nro_part
    dato["nombre"] = nombre
    dato["apellido"] = apellido
    dato["edad"] = edad
    dato["sexo"] = sexo
    dato["disparo1"] = disparo1
    dato["disparo2"] = disparo2
    dato["mejor_disparo"] = mejor_disparo
    

    participantes.append(dato)
    
    
print(participantes)


ganador = 9999
part_ganador = ""
for item in participantes:
    if item["mejor_disparo"] < ganador:
        ganador = item["mejor_disparo"]
        part_ganador = item["nro_part"]
        
for item in participantes:
    if item["nro_part"] == part_ganador:
        print("El participante ganador es:")
        print(item)


perdedor = 0
part_perdedor = ""
for item in participantes:
    if item["mejor_disparo"] > perdedor:
        perdedor = item["mejor_disparo"]
        part_perdedor = item["nro_part"]
        
for item in participantes:
    if item["nro_part"] == part_perdedor:
        print("El participante perdedor es:")
        print(item)


print("Cantidad de participantes: {}".format(cant_part))

for item in participantes:
    if item["sexo"] == "f":
        cant_mujeres = cant_mujeres + 1
        
print("Cantidad de mujeres: {}".format(cant_mujeres))        

cant_hombres = cant_part - cant_mujeres

for item in participantes:
    if item["sexo"] == "m":
        prom_edadhom  = prom_edadhom  + item["edad"]
        
print("promedio de edad de los hombres: {}".format(prom_edadhom/cant_hombres))


for item in participantes:
    prom_disparos = prom_disparos + item["disparo1"] + item["disparo2"]
    
print("Promedio de disparo: {}".format(prom_disparos/cant_part))
        

for item in participantes:
    prom_mejordisp = prom_mejordisp + item["mejor_disparo"]
    
print("Promedio de mejores disparos: {}".format(prom_mejordisp/cant_part))
    
#with open("participantes.csv", "w", newline="") as archivo_participantes:
    #obj = csv.writer(archivo_participantes)
            
    #for item in participantes:
    #    obj.writerow(list(item))
    