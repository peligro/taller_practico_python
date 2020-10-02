import os
import shutil


#ruta = "/var/www/html/clientes/tamila/videotutoriales/python/repo/clase_14/"

ruta = os.path.dirname( os.path.abspath( __file__ )) 

#obtener la ruta del archivo actual
archivo_actual = os.path.abspath( __file__ )

#mostrar el path del directorio de trabajo del Sistema operarivo (linux)
directorio_de_trabajo = os.getcwd()

#print(directorio_de_trabajo)

#crear carpeta
if not os.path.isdir( ruta+"/mi_carpeta" ):
    os.makedirs(ruta+"/mi_carpeta")


#listar el contenido de una carpeta
#print(os.listdir(ruta))

#renombrar una carpeta
#os.rename( ruta+"/hola", ruta+"/chao" )

#eliminar una carpeta vacía
#os.rmdir(ruta+"/chao")

#eliminar una carpeta que tenga contenido, de forma recursiva
if os.path.isdir(ruta+"/chao"):
    shutil.rmtree(ruta+"/chao")

#copiar un archivo
shutil.copy( ruta+"/hola.html", ruta+"/chao.html" )

#mover un archivo
shutil.move( ruta+"/hola.html", ruta+"/mi_carpeta/archivo_guardado.html" )
