import sqlite3

conexion = sqlite3.connect("mi_db.sqlite3")

cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nombre VARCHAR(50) UNIQUE,
        precio INTEGER, 
        descripcion VARCHAR(120)
    )
''')

cursor.execute("INSERT INTO productos VALUES (NULL, 'Portatil', 749, 'PC de sobremesa')")

variosProductos = [
    ('Camiseta', 10, 'Deportes'),
    ('Jarrón', 90, 'Cerámica'),
    ('Camión', 20, 'Juguetería')
]

cursor.executemany("INSERT INTO productos VALUES (NULL, ?,?,?)", variosProductos)

cursor.execute("UPDATE productos SET precio=35 WHERE nombre='Camiseta'")
cursor.execute("DELETE FROM productos WHERE nombre='Camión'")

cursor.execute("SELECT * FROM productos")

lista_campos = cursor.fetchall()

for producto in lista_campos:
    print(producto)
    #print("Nombre": ", producto[0])

conexion.commit()

conexion.close()