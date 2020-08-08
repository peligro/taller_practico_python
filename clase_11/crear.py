import pandas as pd 
from pandas import ExcelWriter

ruta = "/var/www/html/clientes/tamila/videotutoriales/python/clase_11/"

datos = pd.DataFrame({
    'id': [1, 2 , 3, 4, 5],
    'nombre':['Juan', 'Eva', 'María', 'Pablo', 'César'],
    'apellido':['Méndez', 'López', 'Tito', 'Hernández', 'Cancino']
})

#formalizamos las filas
datos = datos[['id', 'nombre', 'apellido']]

writer  = ExcelWriter(ruta+ 'archivo.xlsx')

datos.to_excel(writer, 'Hoja 1', index=False)

writer.save()

