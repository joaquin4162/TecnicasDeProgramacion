#escribir una funcion que, dado un string, reornte la longitud de la palabra mas larga,
#se considera que las palabras estan separadas por uno o mas espacion
#tmb puede haber espacios al principio o al final del string pasado por el parametro

"hola mundo"
" hola mundo"
" hola  mundo "

def largoPalabraMasLarga(frase):
    if len(frase) == 0:#evalua el largo del string
        return 0
    
    longitud = 0
    long_max = 0
    indice = 0
    while indice < len(frase):
        if frase[indice] != " ":
            longitud += 1 #longitud - longitud + 1
        
        if frase[indice] == " " or indice == len(frase)-1:
            if longitud > long_max:
                long_max = longitud
            longitud = 0
        indice += 1
    return long_max
            
            

largo_max_palabra = largoPalabraMasLarga("soy el mas govir equis de")

print(largo_max_palabra)
