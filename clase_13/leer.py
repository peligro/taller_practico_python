import json

ruta = "/var/www/html/clientes/tamila/videotutoriales/python/repo/clase_13/"

with open(ruta+'ejemplo.json') as file:
    datos = json.load(file)
    

for dato in datos['post']:
    print(f"id={dato['id']}\ntítulo={dato['titulo']}\detalle={dato['detalle']}\nfecha={dato['fecha']}")
    print('-----------------')