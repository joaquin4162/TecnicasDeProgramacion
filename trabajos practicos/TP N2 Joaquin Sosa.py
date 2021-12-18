dato = {
    "DNI": "",
    "Nombre": "",
    "Apellido": "",
    "Sucursal": "",
    "Edad": "",
    "SueldoBasico": "",
    "Premios": "",
    "Descuentos": "",
        }
empleados = []
cant_empleados = 0
SueldoBasicoSuma = 0


while True:       #Punto 1
    
    DNI = int(input("Ingrese Dni: "))
    if DNI == 999:
        break
    Nombre = input("Nombre: ")
    Apellido = input("Apellido: ")
    Sucursal = input("Sucursal: ")
    Edad = int(input("Edad: "))
    SueldoBasico = int(input("Sueldo Basico($): "))
    Premios = int(input("Premio($): "))
    Descuentos = int(input("Descuento(%): "))
    
    SueldoBasicoSuma = SueldoBasicoSuma + SueldoBasico
    cant_empleados = cant_empleados + 1
    
    dato = {
        "DNI": "",
        "Nombre": "",
        "Apellido": "",
        "Sucursal": "",
        "Edad": "",
        "SueldoBasico": "",
        "Premios": "",
        "Descuentos": "",
        }
    
    dato["DNI"] = DNI
    dato["Nombre"] = Nombre
    dato["Apellido"] = Apellido
    dato["Sucursal"] = Sucursal
    dato["Edad"] = Edad
    dato["SueldoBasico"] = SueldoBasico
    dato["Premios"] = Premios
    dato["Descuentos"] = Descuentos
    #Punto 2
    dato["SueldoNeto"] = (SueldoBasico + Premios) - (Descuentos*(SueldoBasico + Premios)) / 100
    
   
    empleados.append(dato)
   
    



#Punto 4
print("Cantidad de empleados cargados: {}".format(cant_empleados))    

#Punto 3
print(empleados)
sueldoNeto1 = 0
MayorSueldoNeto = ""
for item in empleados:
    if item["SueldoNeto"] > sueldoNeto1:
        sueldoNeto1 = item["SueldoNeto"]
        MayorSueldoNeto = item["DNI"]

for item in empleados:
    if item["DNI"] == MayorSueldoNeto:
        print("Empleados con mayor sueldo neto: ")
        print(item)
        
sueldoNeto2 = 99999999999999
MenorSueldoNeto = ""
for item in empleados:
    if item["SueldoNeto"] < sueldoNeto2:
        sueldoNeto2 = item["SueldoNeto"]
        MenorSueldoNeto = item["DNI"]

for item in empleados:
    if item["DNI"] == MenorSueldoNeto:
        print("Empleados con Menor sueldo neto: ")
        print(item)
        

#Punto 5
MayoresCuarenta = 0
for item in empleados:
    if item["Edad"] >= 40:
        MayoresCuarenta = MayoresCuarenta + 1

print("Porcentaje de empleados mayores de 40(%): {}".format((MayoresCuarenta*100)/cant_empleados))

#Punto 6

premio1 = 99999999999999
MenorPremio = ""
for item in empleados:
    if item["Premios"] < premio1:
        premio1 = item["Premios"]
        MenorPremio = item["DNI"]

for item in empleados:
    if item["DNI"] == MenorPremio :
        print("Sucursal de empleado con menos premio: {}".format(item["Sucursal"]))

#punto 7
#SueldoBasePromedio = SueldoBasicoSuma / cant_empleados
#EmpSueldoMenorProm = []
