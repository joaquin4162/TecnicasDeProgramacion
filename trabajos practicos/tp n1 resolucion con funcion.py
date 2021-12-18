
def bonificacion(sbasico, bonif, tipo):
    if tipo == "$":
        bonifpesos = bonif
    else:
            bonifpesos = sbasico * bonif / 100
    total = sbasico + bonifpesos   
    return total

cant = 0
acum = 0
cont = 0
acumsueldos = 0
basico = int(input("Ingrese el sueldo basico: "))

while basico != 0:
  
    bonif = int(input("Ingrese la bonificacion: "))
  
    tipo = str(input("Ingrese el tipo(%/$): "))
  
  
    acum = acum + basico
   
    cant = cant + 1
    
    if bonif > 0:
        cont = cont + 1
    
    resultado = bonificacion(basico, bonif, tipo)
  
    acumsueldos = acumsueldos + resultado
        

    basico = int(input("Ingrese el sueldo basico: "))
    
    

print("Cantidad de empleados: {}".format(cant))
print("Promedio de basicos: {}".format(acum/cant))
print("porcentaje de empleados con bonif: {}%".format(cont/cant*100))
print("Total pagado a los empleados: {}".format(acumsueldos))



