#sets y diccionarios

usuario = {"César", "Juan", "María", 12}
miSet= {
        "nombre":"César",
        "apellido":"Cancino",
        "edad":40,
        "nacionalidad":"chileno"
    }
print(type(miSet))
#print(type(usuario))
print(usuario)
usuario.add(True)
print(usuario)
#JSON 
#un diccionario es un conjunto de sets
contactos =[
    {
        "nombre":"César",
        "apellido":"Cancino",
        "edad":40,
        "nacionalidad":"chileno"
    }
]
print(type(contactos))