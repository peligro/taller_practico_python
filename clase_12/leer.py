from xml.dom import minidom

ruta= "/var/www/html/clientes/tamila/videotutoriales/python/clase_12/"

xml = minidom.parse(ruta+"ejemplo.xml")

docs = xml.getElementsByTagName("doc") 

for doc in docs:
    nodo1 = doc.getElementsByTagName("nodo1")[0]
    nodo2 = doc.getElementsByTagName("nodo2")[0]
    print(f"nodo1={nodo1.firstChild.data} | nodo2={nodo2.firstChild.data}")




"""
<root>
    <doc>
        <nodo1 name="nodo">Texto nodo1</nodo1>
        <nodo2 atributo="manzana">Texto nodo2</nodo2>
    </doc>
</root>
"""