import requests

endpoint = "http://localhost/clientes/tamila/v1/personas"

payload = {"nombre":"Miguel Gutuérrez", "correo":"miguelito@yahoo.es", "telefono":"+584165452142"}

cabeceros = {'content-type': 'application/json', 'token':'123456'}

response= requests.post(endpoint, headers=cabeceros, json=payload)

print(response.text)