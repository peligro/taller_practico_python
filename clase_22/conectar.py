import mysql.connector

#establecer la conexión a la BD
database = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'peligro',
    passwd = '123456',
    database = 'pruebas_python' 
)

cursor = database.cursor( buffered=True )