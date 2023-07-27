#!/usr/bin/python
 
import MySQLdb
 
print "Content-Type: text/html"
print
print "<html><head><title>Libros</title></head>"
print "<body>"
print "<h1>Los ultimos 10 libros</h1>"
print "<ul>"
 
conexion = MySQLdb.connect(user='yo', passwd='dejame_entrar', db='mi_base')
cursor = conexion.cursor()
cursor.execute("SELECT nombre FROM libros ORDER BY fecha_pub DESC LIMIT 10")
for fila in cursor.fetchall():
    print "<li>%s</li>" % fila[0]
 
print "</ul>"
print "</body></html>"

conexion.close()