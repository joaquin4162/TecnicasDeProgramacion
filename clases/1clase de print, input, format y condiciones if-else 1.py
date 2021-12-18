#comentarios, dejar mensajes de ayuda o de guia
print("hola mundo")
print("aca estoy")
print('texto con con comillas simples')

mi_variable = 5

pepito = 30 #las variables pueden ser numericas (int o float)
pepita ="30" #o palabras (string, str)

dato = 56.0

frase = "esta es una frase"

print(mi_variable) #imprimir el contenido de una variable
print(frase)
print("frase") #imprimo algo en pantalla entre comillas

resultado = pepito + dato + 1000
print(resultado)

resultado2 = pepito - mi_variable
print(resultado2)

resultado3 = frase + " _hola_ " + pepita #concatenacion (solo con string)
print(resultado3)

resultado4 = pepito + int(pepita)  #casteo (sabemos que pepita es un numero)
print(resultado4)
#puedo castear int float (casteo un string en un nuemero)
#str -> casteo un entero en string

resultado5 = str(pepito) + pepita
print(resultado5)

print("el resultado es: {}".format(resultado2)) #format sustituye el interior de las llaves
#el orden de las llaves respeta el orden de los format
#format sirve para mostrar el contenido de una variable dentro del texo
print("el resultado es: {} - {}".format(resultado2, resultado))

#ingresar con teclado
print("bienvenido")

resultado6 = input("ingrese su contraseña") #funcion bloqueante, por que espera
#que alguien ingrese algo por teclado

print("usted ingreso: {}".format(resultado6))
edad = input("Ingrese su edad: ")
print("usted tiene {} años".format(edad))

print('saliendo del programa')
#input siempre retorna lo que ingrese con teclado como un dato tipo str
#entonces el dato edad nunca se va a poder sumar como un entero
#pero si definimo int(input(""), se convierte en un entero

                    #condiciones if;else-------if:verdadero :else:falaso
print("bienvenido")

edad = int(input("Ingrese su edad: "))
print("usted tiene {} años".format(edad))

if edad > 18:  #if se escribe la condicion y se ponen ":"
    print("es mayor de edad")
    print("estoy drento del if true")
else:  #else se escribe la condicion y se pone ":" si no tira error
    print("es menor de edad")
    print("estoy dentro del else")
    
print('saliendo del programa')
