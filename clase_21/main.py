import os 
import sqlite3


ruta = os.path.dirname(os.path.abspath(__file__))

#conectamos a la base de datos. (En realidad en el caso de sqlite creamos el fichero)
conection = sqlite3.connect( ruta + "/manosenelcodigo.db" )

cursor = conection.cursor()


#creamos una tabla
crearTabla = """
    create table if not exists productos(
        id integer primary key autoincrement,
        titulo varchar(100),
        descripcion text,
        precio int(100)
    )    
"""

cursor.execute(crearTabla)
conection.commit()


#crear un  registro

insertarRegistro = """
    insert into productos values (null, 'Mesa portátil', 'es una mesa que se mueve y se menea con ñandú', 2345)
"""
cursor.execute(insertarRegistro)
conection.commit()

#crear varios registros
varios = [
    ('Flores verdes', 'son flores bonitas', 123),
    ('Ron Pampero', 'con coca cola es lo mejor', 6576),
    ('Tallarín salteado con pollo', 'para desmayarse del sabor', 3456)
]

insertarRegistro2 = """
    insert into productos values (null, ?, ?, ? )
"""
cursor.executemany(insertarRegistro2, varios)
conection.commit()

#listar registros
listarRegistros = "select * from productos;"
cursor.execute(listarRegistros)

productos = cursor.fetchall()

for producto in productos:
    print(f"id={producto[0]} | título = {producto[1]} | descripción = {producto[2]} | precio={producto[3]}")


#listar un sólo registro
unSoloRegistro = "select * from productos where id=9"
cursor.execute(unSoloRegistro)
primero = cursor.fetchone()
print("-----------------------")
print(primero)

#cerrar la conexión
conection.close()