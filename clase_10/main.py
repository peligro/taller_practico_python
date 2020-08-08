from xhtml2pdf import pisa
from jinja2 import Template
import os


ruta= "/var/www/html/clientes/tamila/videotutoriales/python/clase_10/"

sourceHtml= open( os.path.join(ruta, 'ejemplo.html') ).read()

outputFilename = ruta + "ejemplo.pdf"
data = {"nombre":"César Cancino", "ruta": ruta}

resultFile = open(outputFilename, "w+b")
#pisaStatus = pisa.CreatePDF(sourceHtml, dest=resultFile)

template = Template(open(os.path.join( ruta, 'ejemplo.html' )).read())
html = template.render(data)
pisaStatus = pisa.CreatePDF( html, dest=resultFile )

resultFile.close()

