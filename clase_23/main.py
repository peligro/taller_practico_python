import psycopg2#sudo apt-get install python3-psycopg2


#establecemos la conexión
conexion = psycopg2.connect(database="python", user="peligro", password="123456")
cursor = conexion.cursor()

#crear registros
insertar = "insert into python.productos (nombre, precio) values (%s, %s);"
#insertar = "insert into python.productos values (%s, %s);"
parametros = ("Pollo asado", "3500")
#cursor.execute(insertar, parametros)
#conexion.commit()


#listar registros
sql = "select * from python.productos;"
cursor.execute(sql)
for dato in cursor:
    print(f"id={dato[0]} | nombre={dato[1]} | precio={dato[2]}")