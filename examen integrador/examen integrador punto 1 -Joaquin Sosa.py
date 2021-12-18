def bonos(sueldobasico, antiguedad):
    if antiguedad >= 1 and antiguedad <= 5:
        sueldoconbono = (10 * sueldobasico) / 100
      
    elif antiguedad >= 6 and antiguedad <= 10:
        sueldoconbono = (20 * sueldobasico) / 100
      
    elif antiguedad > 10:
        sueldoconbono = (30 * sueldobasico) / 100
      
    else:
        sueldoconbono = 0
    
    total = sueldoconbono + sueldobasico
    
    return total




sueldobasico = int(input("Ingrese sueldo basico($): "))

num_empleados = 0

cantidad_sueldos = 0

cantidad_antiguedad = 0

cant_mujeres = 0

can_sueldobono = 0

sueldototal_mayor = 0

mayor_edad = 0

menor_edad = 999

while sueldobasico != 0:
    
    num_empleados += 1
    
    cantidad_sueldos = cantidad_sueldos + sueldobasico
    
    edad = int(input("Ingrese edad: "))
    
    if edad > mayor_edad:
        mayor_edad = edad
    
    if edad < menor_edad:
        menor_edad = edad
   
    sexo = input("Ingrese sexo (f/m): ")
    
    if sexo == "f":
        cant_mujeres += 1
       
    antiguedad = int(input("Ingrese antigüedad(años): "))
    
    cantidad_antiguedad = cantidad_antiguedad + antiguedad
    
    resultado = bonos(sueldobasico, antiguedad)
    
    can_sueldobono = resultado + can_sueldobono
    
    if resultado > sueldototal_mayor:
        sueldototal_mayor = resultado
    

    sueldobasico = int(input("Ingrese sueldo basico($): ")) 


print("Cantidad de empleados ingresados: {}".format(num_empleados))    

print("Sueldo Basico promedio: {}".format(cantidad_sueldos / num_empleados))    

print("Antigüedad promedio de los empleados: {}".format(cantidad_antiguedad / num_empleados))

print("Porcentaje de mujeres trabajando(%): {}".format((cant_mujeres*100)/num_empleados))

print("Sueldo total promedio (basico + bono): {}".format(can_sueldobono / num_empleados))

print("Sueldo total mas alto: {}".format(sueldototal_mayor))

print("Empleado con mayor edad: {}".format(mayor_edad))

print("Empleado con menor edad: {}".format(menor_edad))


