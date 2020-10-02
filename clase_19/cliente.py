import requests

endpoint = "http://localhost/clientes/tamila/v1/personas"


cabeceros = {'content-type': 'application/json', 'token':'123456'}

response= requests.get(endpoint, headers=cabeceros)

print(response.text)