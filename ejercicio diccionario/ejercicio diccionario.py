#suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes,
#la cual contiene tuplas con informacion de cada venta:(cliente,dia del mes, monto, domicilio dle cliente)
#escribir una funcion que reciba como parametro una lista con el formato mencionado anteriormente y
# retorne los domicilios de cada ciente al cual se le debe enviar una futura compra
#notar que cada cliente puede haber hecho mas de una compra al mes
#por lo que la funcion debe retornar una estructura que contenga cada domicilio una sola vez
#adicionar el calcul odel total de la compra realizada por cada cliente


listaFacturas = [("Juan Gonzalez", 5, 100, "Bonificio 34"),
                   ("Jose Lopez", 7, 700, "Libertador 218"),
                   ("Juan Gonzalez", 7, 500, "Bonificio 34"),
                   ("Julian Rodriguez", 12, 5000, "La Mancha 761"),
                   ("Jose Lopez", 15 , 900, "Libertador 218")]
                   

def domiciliosFactura(lista):
    domicilios = []
    for item in lista:
        if item[3] not in domicilios:
            domicilios.append(item[3])
    return domicilios

domicilios = domiciliosFactura(listaFacturas)

print(domicilios)