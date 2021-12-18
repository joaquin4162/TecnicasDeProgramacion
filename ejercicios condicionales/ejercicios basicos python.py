#Escribir un programa que le pregunte al usuario su nombre y edad, y luego lo salude.

nombre = input("Ingrese su nombre:")
edad = int(input("Ingrese su edad:"))

print("su nombre es: {}".format(nombre))
print("su edad es: {}".format(edad))

print("Mucho gusto")

#Calcular el perímetro y área de un rectángulo ingresando su base y altura.

base = int(input("valor de la base:"))
altura = int(input("valor de la altura"))

perimetro = base * 2 + altura * 2

print("el perimetro es: {}".format(perimetro))

#Dado los catetos de un triángulo, calcular la hipotenusa.

cateto1 = int(input("ingrese cateto 1:"))
cateto2 = int(input("ingrese cateto 2:"))

hipotenusa = cateto1 ** 2 + cateto2 ** 2

print("hipotenusa:{}".format(hipotenusa))

#Escribir un programa que pregunte al usuario por el número de horas trabajadas y el costo por hora
# Después debe mostrar por pantalla la paga que le corresponde

print("bienvenido")
nombre_y_apellido = input("ingrese su nombre y apellido:")

print("trabajador verificado:{}".format(nombre_y_apellido))

horas = int(input("ingrese horas trabajadas:"))

precio_por_hora = 500

print("precio por hora:{}".format(precio_por_hora))
sueldo = horas * precio_por_hora

print("su paga es de:${}".format(sueldo))
