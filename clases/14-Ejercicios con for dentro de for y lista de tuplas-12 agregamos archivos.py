#Escribir un programa que permita procesar datos de pasajero de viajes  en una
#lista de tuplas (nombre,dni,ciudaddestino)
#Ademas en otro lista de tuplas almacenar los datos de cada ciudad y el pais al que pertenecen
#mostrar un menu para que realice las sig operaciones
#1- Agregar pasajero a la lsita de viajeros
#2Agregar ciudades a la lsita de ciudades
#3Dado el dni de un pasajero ver a que ciudad viaja
#4 dada una ciudad mostrar la cantidad de pasajeros que viajan a esas ciudad
#5dado el dni de un pasajero ver a que pais viaja
#6 dado un pais, mostrar cuantos pasajeros viajan a este pasi
#7 guardar en archivo
#8 leer desde archivo
#9 terminar


import csv



pasajeros = [("Joaquin", 100, "Mendoza"), ("Maximo", 300, "Misiones"), ("Elias", 200, "Asuncion")]
ciudades = [("Mendoza", "Argentina"), ("Misiones", "Argentina"), ("Asuncion", "Paraguay")]

while True:
    opcion = int(input("Ingrese opcion (1-9): "))
    
    if opcion == 1:
        nombre = input("Ingrese nombre: ")
        dni = int(input("Ingrese dni: "))
        ciudad = input("Ingrese ciudad destino: ")
        
        registro = (nombre, dni, ciudad)
        
        pasajeros.append(registro)
    elif opcion == 2:
        ciudad = input("Ingrese la Ciudad: ")
        pais = input("Ingrese el pais: ")
        
        registro = (ciudad, pais)
        ciudades.append(registro)
    elif opcion == 3:
        dni = int(input("Ingrese dni: "))
        encontrado = False
        for pasajero in pasajeros:
            if pasajero[1] == dni:
                print("El pasajero {} viaja a {}".format(pasajero[0], pasajero[2]))
                encontrado = True
            
        if not encontrado:
            print("El dni no se cuentra")
            
    elif opcion == 4:
        contador = 0
        ciudad = input("Ingrese la ciudad: ")
        for pasajero in pasajeros:
            if pasajero[2] == ciudad:
                contador = contador + 1
        print("viajan {} pasajeros a {}".format(contador, ciudad))
    elif opcion == 5:
         dni = int(input("Ingrese dni: "))
         for pasajero in pasajeros:
             if pasajero[1] == dni:
                 for ciudad in ciudades:
                     if ciudad[0] == pasajero[2]:
                         print("EL pasajero {} viaja a {}".format(pasajero[0], ciudad[1]))
    elif opcion == 6:         
        contador1 = 0
        pais = input("Ingrese el pasi: ")
        for ciudad in ciudades:
            if ciudad[1] == pais:
                for pasajero in pasajeros:
                    if pasajero[2] == ciudad[0]:
                        contador1 += 1
                        
        if contador1 > 1:
            print("{} pasajeros viajan a {}".format(contador1, pais))
        else:
            print("{} pasajers viaja a {} ".format(contador1, pais))
                            
    elif opcion == 7:
        
        with open("pasajeros.csv", "w", newline="") as archivo_pasajeros:
            obj = csv.writer(archivo_pasajeros)
            
            for item in pasajeros:
                obj.writerow(list(item))
    
    elif opcion == 8: 
        with open("pasajeros.csv", "r") as archivo_pasajeros:
            contenido_csv = csv.reader(archivo_pasajeros)
            for row in contenido_csv:
                print("{} {} tuvo la siguiente nota {}".format(row[0],row[1],row[2]))
    elif opcion == 9:
        break
    print("pasajeros: ",pasajeros, "ciudades: ", ciudades)