import collections

tuplas=(20,30)
lista=[20,30]
diccionario={"llave1":20,"llave2":30}

for item in tuplas:
    print(item)

for item in lista:
    print(item)

for llave in diccionario:
    print(diccionario[llave])

class Productos(collections.Iterable):
    pass

listadoproductos=Productos()

for item in listadoproductos:
    print(item)