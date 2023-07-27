from io import open
#write
archivo_texto=open("archivo.txt", "w")
frase="El método open() usado en modo escritura \n crea el archivo si no existe"
archivo_texto.write(frase)
archivo_texto.close()

#read
archivo_texto=open("archivo.txt", "r")
texto=archivo_texto.read() # también podemos usar readlines() para guardar las lineas en una lista
archivo_texto.close()
print(texto)

#append
archivo_texto=open("archivo.txt", "a")
archivo_texto.write("Una nueva linea")
archivo_texto.close()

#mover el cursor con seek()
archivo_texto=open("archivo.txt", "r")
#archivo_texto=open("archivo.txt", "r+") # lectura y escritura
print(archivo_texto.read())
print(archivo_texto.read())
archivo_texto.seek(5)
#archivo_texto.seek(len(archivo_texto.read())/2) # obtenemos la mitad de la longitud del archivo de texto
#archivo_texto.seek(len(archivo_texto.readline())) # situamos el cursor al final de la primera linea
print(archivo_texto.read())