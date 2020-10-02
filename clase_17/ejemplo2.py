import time
from jose import jwt

ts = int(time.time())
secreto = "secreto1"

token = jwt.encode({'id': '1', 'nombre': 'Cesar Cancino', 'time':ts}, secreto, algorithm='HS256')

resuelto=jwt.decode(token, secreto, algorithms=['HS256'])
print("------------------")
print(token)
print("-----resuelto-------")
print(resuelto)