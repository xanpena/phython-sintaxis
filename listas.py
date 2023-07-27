# -+- coding: utf-8 -*-
colores = list()
colores.append('rojo')
colores.append('azul')
colores.append('amarillo')

colores.insert(2, "verde")

print(milista[:])

print(milista.index("rojo"))

colores.extend(['Marron', 'naranja', 'Violeta'])

colores.remove("amarillo")
colores.remove(2)

colores.pop()

print(colores)
print(colores[1])

print(type(colores))
id(colores)

colores.sort(key=str.lower)
