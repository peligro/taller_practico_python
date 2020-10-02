from suds.client import Client

url="http://www.otravuelta.cl/soap/index.php?wsdl"

cliente = Client(url)
#print(cliente)


resultados = cliente.service.retornarDatos("César Cancino", "yo@cesarcancino.com", "+56961709937")
print(resultados)