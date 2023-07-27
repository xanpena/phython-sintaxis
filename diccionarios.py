mi_diccionario = {}
mi_diccionario['primer_elemento'] = 'primer valor'

print(mi_diccionario)
print(mi_diccionario['primer_elemento'])


mi_diccionario2 = dict()

calificaciones = {}
calificaciones['algoritmos'] = 9.00
calificaciones['automatas'] = 5.45
calificaciones['matematicas'] = 7.37
calificaciones['programacion'] = 10.00
calificaciones['bases_de_datos'] = 6.34

for key in calificaciones:
    print(key)

for key in calificaciones.values():
    print(key)

for key, value in calificaciones.items():
    print('LLave: {}, valor: {}'.format(key, value))

# manejando error KeyError si no existe la llave
print(calificaciones.get('helado', None)) 

# en un diccionario no puede haber dos claves iguales
paises={"Alemania":"Berlín", "Francia":"París", "Italia":"Roma"}
print(paises)
paises['España'] = 'Lisboa'
paises['España'] = 'Madrid'
print(paises)
del paises["Alemania"]
print(paises)
print(paises.keys())
print(paises.values())