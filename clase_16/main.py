import ftplib
import os


#establecer la conexión
ftp = ftplib.FTP("192.168.0.12", "cesar", "123456")

#listar los archivos del servidor al cual me conecté vía FTP
files = ftp.dir()
print(files)

#descargar archivos del FTP
ruta = os.path.dirname(os.path.abspath(__file__))

try:
    ftp.retrbinary("hola.py", open(ruta+ "/holassss.py" , "wb").write)
except Exception as e:
    print("error")

#subir archivos al FTP

try:
    ftp.storbinary("STOR "+ "chola.jpg", open(ruta+"/chola.jpg", "rb"))
except Exception as e:
    pass