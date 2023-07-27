import pickle

nombres = ['Xan', 'Ana', 'Pablo', 'Teresa']

fichero_binario = open('binario', "wb")

pickle.dump(nombres, fichero_binario)

fichero_binario.close()

del(fichero_binario) # borramos de memoria

# acceder al contenido

fichero = open("binario", "rb")

lista = pickle.load(fichero)

print(lista)