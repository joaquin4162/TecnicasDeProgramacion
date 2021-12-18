clientes = []
cont = 0

def domiciliosFactura(lista):
    domicilios = []
    for item in lista:
        if item["domicilio"] not in domicilios:
            domicilios.append(item["domicilio"])
        
    return domicilios



while True:
    cliente = input("cliente: ")
    if cliente == "":
        break
    
    dia = int(input("Dia del mes: "))
    monto = int(input("Monto: "))
    domicilio = input("Domicilio: ")
    
    cont = cont + 1
    
    dato = {
        "cliente": "",
        "dia": "",
        "monto": "",
        "domicilio": ""
        }
    
    dato["cliente"] = cliente
    dato["dia"] = dia
    dato["monto"] = monto
    dato["domicilio"] = domicilio
    
    clientes.append(dato)
    
print(clientes)
#la funcion domiciliosFactura me retorna una lista con Domicilios
respuesta = domiciliosFactura(clientes)

print(respuesta)

data = {}
for item in respuesta:
    data[item] = 0
    
    for i in clientes:
        if i["domicilio"] == item:
            data[item] = data[item] + i["monto"]
            
            
print(dato)