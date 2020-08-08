# lista es una variable que permite almacenar más de un valor
# las listas o los diccionarios serían el equivalente a los arrays

nombre1 = 'César Cancino'

#tenemos una lista de largo 6
#esta lista es de carácter unidimensional
miListas = [ 'César', 30, 4.4, True, "Texto", 56]
#print(miListas)
#obtener el largo de una lista o la cantidad de registro de la misma
#print(len(miListas))
nombres = ['César', 'Juan', 'Pedro', 'Joel', 'Helena', 'María', 'Sofía']
#print(f"el largo de mi lista es {len(nombres)}")
#print(nombres[6])
#se agrega un valor al final de la  lista
nombres.append('Andŕes')
#print(f"el largo de mi lista es {len(nombres)}")
#print(nombres)
nombres.insert(0, 'Jesús')
#print(nombres)
#print(nombres[-1])
anios = list(range(1980, 2020))
#print(anios)
#print(type(nombres))
#recorrer una lista
for nombre in nombres:
    print(f"{nombres.index(nombre)}  nombre: {nombre}") 