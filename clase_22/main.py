from conectar import database, cursor

#creamos una tabla
crearTabla = """
    create table if not exists productos(
        id int(10) not null auto_increment primary key,
        titulo varchar(100),
        descripcion text,
        precio int(10),
        fecha datetime 
    );
"""

cursor.execute(crearTabla)

#crear un registro
insertar = " insert into productos values (null, 'Mesa portátil', 'una mesa bonita con ñandú', 345, now()); "
cursor.execute(insertar)
database.commit()

#crear varios registros

insertVarios = """
    insert into productos values (null, %s, %s, %s , now());
"""
varios = [
    ('Flores de bag', 'flores olorosas', 123),
    ('Leche sin lactosa de chocolate', 'es sanita para el estómago', 5567),
    ('Pechuga de pollo', 'mi descripción con ñandú', 2345),
]

cursor.executemany(insertVarios, varios)
database.commit()

#listar 
cursor.execute("select * from productos;")
productos = cursor.fetchall()
#print(productos)
for producto in productos:
    print(f"id={producto[0]} | título = {producto[1]} | descripción = {producto[2]} | precio={producto[3]} | fecha={producto[4]}")

#listar un sólo registro
cursor.execute("select * from productos where id=1 ")
primero = cursor.fetchone()
print("-------------------------")
print(primero)

