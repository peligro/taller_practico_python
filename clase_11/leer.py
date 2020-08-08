import xlrd

ruta = "/var/www/html/clientes/tamila/videotutoriales/python/clase_11/"

documento = xlrd.open_workbook(ruta+'archivo.xlsx')

datos = documento.sheet_by_index(0)

for i in range(datos.nrows):
    if i>=1:
        print(f"ID={repr(datos.cell_value(i, 0))} | Nombre:{repr(datos.cell_value(i, 1))} | Apellido:{repr(datos.cell_value(i, 2))} ")