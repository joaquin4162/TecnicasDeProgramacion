"COmo iterar un diccionario"

dic = {'nombre' : 'joaquin', "apellido" : "sosa", "edad" : 23, 34.4 : None}


for item in dic: #cuando barro un diccionario de esta forma, me devulve las key
    print(item)
    
    
print("____________________")   


for item in dic:
    print(item)
    print(dic[item])
    
print("____________________")   


for a in dic.values(): # aca me devueve solo los values
    print(a)

print("____________________")   


for a,b in dic.items():  # me retorna 2 datos, primero la key, y luego los values
    print(a, b)
    
print("____________________")   

dic = {
       'nombre' : '', 
       "apellido" : "",
       "edad" : None 
       }
registro = []   # lista de un diccionario

while True:
    nom = input("ingrese nombre: ")
    ape = input("ingrese apellido: ")
    edad = int(input("ingrese edad: "))

    dic["nombre"] = nom
    dic["apellido"] = ape
    dic["edad"] = edad
    
    registro.append(dic)
    
    dic = {
       'nombre' : '', 
       "apellido" : "",
       "edad" : None 
       }
    
    opcion = input("desea seguis (S/N): ")
    if opcion == "n":
        break
  
print(registro)


for item in registro:#cada item es un diccionario
    if item["edad"] > 18:
        print(item["edad"]) # aca  accedo a cada edad de cada lista
    

    