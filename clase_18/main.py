import requests
import re

url = "http://localhost/clientes/tamila/test/python/scraper/test.php" #endpoint

response = requests.get(url)

#print(response.status_code)

if response.status_code==200:#es decir, si la petición HTTP es correcta
    contenido = response.text
else:
    print("ocurrió un error o lo que sea")


regex = '<div class="price">(.+?)</div>'
for precio in re.findall(regex, contenido):
    print(f"el precio es {precio[1:len(precio)]}")