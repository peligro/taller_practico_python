from datetime import datetime, date, time, timedelta
from utilidades import *

ahora = datetime.now()
#print(type(ahora))
#print(ahora.utcnow())
#2020-08-04 20:00:00
#print(f"{ahora.year}-{ahora.month}-{ahora.day} {ahora.hour}:{ahora.minute}:{ahora.second}")

#creamos fecha con parámetros
hoy = datetime.today()
formato_date="%Y-%m-%d"
formato_datetime="%Y-%m-%d %H:%M:%S"
print(f"fecha con formato date {hoy.strftime(formato_date)}")
print(f"fecha con formato datetime {hoy.strftime(formato_datetime)}")

#convertir una cadena a un objeto datetime
objeto_datetime = datetime.strptime("2020-08-04", formato_date)
#print(type(objeto_datetime))

#operaciones con fechas  (weeks, days, hours, minutes, seconds, milliseconds y microseconds)
fecha = date.today()
print(fecha)
print(f"fecha menos un día {fecha-timedelta(days=1)}")
print(f"fecha más un día {fecha+timedelta(days=1)}")
print(f"fecha más 2 meses {fecha+timedelta(weeks=20)}")

#diferencia entre dos fechas
fecha1 = datetime.now()
fecha2= datetime(2019, 11, 5, 0, 0, 0)#asignar datetime específica
diferencia= fecha1- fecha2
print(f"hay {diferencia.days} días de diferencia")

#dia de semana
print(f"día de la semana {datetime.weekday(fecha1)}")

#convertir a timestamp
print(f"fecha={fecha1} | timestamp={datetime.timestamp(fecha1)} | convertir de timestamp a datetime {datetime.fromtimestamp(1545730073)}")


print(formateaFecha("2020-05-24"))

