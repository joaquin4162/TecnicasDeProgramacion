dato = {
        "nroPart": "",
        "nombre": "",
        "apellido": "",
        "edad": "",
        "sexo": "",
        "disparo1": "",
        "disparo2": ""
        }

concurso = [] #lista vacia para almacenar los participantes
cantPart = 0
contMasc = 0
acum = 0
acumDisp = 0
#Ciclo de carga
while True:
    
    
    nroPart = int(input("Nro de participante: "))
    if nroPart == 999:
        break
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo (f/m): ")
    disparo1 = int(input("Disparo1: "))
    disparo2 = int(input("Disparo2: "))
    
    cantPart = cantPart + 1
    
        
    dato = {
        "nroPart": "",
        "nombre": "",
        "apellido": "",
        "edad": "",
        "sexo": "",
        "disparo1": "",
        "disparo2": ""
        }


    dato["nroPart"] = nroPart
    dato["nombre"] = nombre
    dato["apellido"] = apellido
    dato["edad"] = edad
    dato["sexo"] = sexo
    dato["disparo1"] = disparo1
    dato["disparo2"] = disparo2
    

    concurso.append(dato)

#procesamiento de informacion

#punto A

ganador = 9999
ganadorID = ""
for item in concurso:
    if item["disparo"] < ganador:
        ganador = item["disparo"]
        ganadorID = item["nroPart"]
        
for item in concurso:
    if item["nroPart"] == ganadorID:
        print("El ganador:")
        print(item)

#punto b

perdedor = 0
perdedorID = ""
for item in concurso:
    if item["disparo"] > perdedor:
        perdedor = item["disparo"]
        perdedorID = item["nroPart"]
        
for item in concurso:
    if item["naroPart"] == perdedorID:
        print("El perdedor:")
        print(item)

#print(dato)
print(concurso)
#punto c
print("cantidad de participantes: {}".format(cantPart))  

#punto d)

for item in concurso:
    if item["sexo"] == "m":
        contMasc = contMasc + 1
        
print("Cantidad de masculinos: {}".format(contMasc))        

#punto E
cantMuj = cantPart - contMasc

for item in concurso:
    if item["sexo"] == "f":
        acum = acum + item["edad"]
        
print("promedio de edad de mujeres: {}".format(acum/cantMuj))

#punto F
for item in concurso:
    acumDisp = acumDisp + item["disparo"]
    
print("Promedio de disparo: {}".format(acumDisp/cantPart))
        