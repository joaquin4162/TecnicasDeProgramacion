#Archivos de texo

#para abrir un archivo usaremos la funcion OPEN

#open() retorna una instancia de la clase FILE la cual podemos ejecutar diversas operaciones

#MODO DE APERTURA DE LOS ARCHIVOS
#1)Solo lectura ("r") En este caso no es posible realizar modificaciones sobre el archivos,
#solemente leer el contenido

archivo = open("prueba.txt")

#resultado = archivo.read()

#print(type(resultado))
#print(resultado)

#res1 = archivo.readline()   #retorna una fila
#while (res1 != ""):
#    print(type(res1))
#    print(res1)
#    
#    res1 = archivo.readline()

res2 = archivo.readlines()    #\n es el codigo del enter #restorna una lista
print(type(res2))
print(res2)

for line in res2:
    print(line)
    
#------------------------------------------------------------------------------------

archivoW = open("prueba_escritura.txt", "w") #crea un archivo y la w indica que es escritura

#archivoW.write("Estoy escribiendo desde python en un archivo...\n") #escribimos en el archivo
#archivoW.write("Segunda linea") 



milista = ["hola desde prueba_escritura.txt\n," 
           "esto es una segunda linea\n",
           "sigo escribiendo\n",
           "Chau"]

archivoW.writelines(milista) #se escrie como una lista



archivoW.close()  #cerramos el archivo


#con la funcion whit open(archivo.txt) as archivo: cierra el archivo automaticamente

