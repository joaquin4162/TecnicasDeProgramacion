#sentencias de bucle "while"
#el bucle se mantiene mientras la concidion se cumpla

i = 1#es un bucle es infinito por que la condicion no cambia i=1

#se pregunta una condicion igual que el if else
while i<= 5:     #ejecuta todas las lineas tabuladas
    print("Holamundo desde Python")#si la condicion es verdadera ejecuta todas las lienas
    i = i + 1 #contador o incrementador de a 1(o cualquier numero)    #cuando termina vuelve a empezar #cuanda la condicion es falsa sale del bucle
 
 
print("---------------------------------------------------")   
 #se trabaja contando el 0 entonces

i = 0

while i < 5: #si usamos <= va contar el 5 tambien
    print("hola mundo desde python")
    i = i + 1
    
print("----------------------------------------------------")

i = 0
acum = 0 #acum acumula
while i < 5 :
    nota = int(input("nota: "))
    
    acum = acum + nota #acum sentencia para acumular, suma todas las notas en este caso
    i = i + 1
    
promedio = acum / 5
print("el promedio de nota es: {}".format(promedio))#no olvidemos que format mete la variable dentro de la llave
print("fin del programa")


print("------------------------------------------------")


print("Bienvenido")
mi_contraseña = "12345"
contraseña = input("Ingrese contraseña: ")

while mi_contraseña != contraseña: #!= significa diferente,cunado la password sea diferente se mete en el bucle
    print("contraseña incorrecta")
    contraseña = input("ingrese nuevamente su contraseña: ")
    
print("saliendo del programa")

print("--------------------------")

#vamos a contar los intentos de contraseñas
print("Bienvenido")
mi_contraseña = "12345"
contraseña = input("Ingrese contraseña: ")
cont = 0

while mi_contraseña != contraseña:
    cont = cont + 1
    if cont == 3:#se puede usar un if dentro de un while y un while dentro de un if
        break   #break me saca del primer bucle presente, si hay muchos bucles, solo te saca de su bloque de bucle
    print("contraseña incorrecta")
    print("le quedan {} intentos".format(3-cont))
    contraseña = input("ingrese nuevamente su contraseña: ")
    
if cont == 3:
    print("tarjeta bloqueada")
else:
    print("Contraseña correcta")
    
print("saliendo del programa")


print("---------------------------------")

i = 0
acum = 0 #acum acumula
nota = int(input("ingrese nota: "))
contProm = 0
contDesap= 0

while (nota <=0 or nota >10) and nota !=99:
    print("nota erronea. Datos validos entre 1 y 10")
    nota = int(input("Ingrese nota nuevamente: "))
while nota != 99 :
    
    acum = acum + nota #acum +=1
    i = i + 1 #acum +=1
    if nota >= 7:
        contProm = contProm + 1
    if nota <4:
        contDesap = contDesap + 1
    nota = int(input("Ingrese nota: "))
    while (nota <=0 or nota >10) and nota !=99:
        print("nota erronea. Datos validos entre 1 y 10")
        nota = int(input("Ingrese nota nuevamente: "))
    
promedio = acum / i #en la variable i tenemos la cantidad de notas que fuimos acumulando
print("Cantidad de notas: {}".format(i))
print("Cantidad de promocione: {}".format(contProm))
print("Cantidad de desaprobados: {}".format(contDesap))
print("el promedio de nota es: {}".format(promedio))
print("fin del programa")