import jwt 
import time

secreto = "123456"
ts = int(time.time())


token = jwt.encode(
    {'id':'1', 'nombre':'César Cancino', 'time':ts},
    secreto,
    algorithm='HS256'
)

resuelto = jwt.decode(token, "22222", algorithms=['HS256'])
print("-------token------")
print(token)
print("-------resuelto------")
print(resuelto)