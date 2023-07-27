# -+- coding: utf-8 -*-

mi_tupla = (1, 2, 3)
mi_lista = [1, 2, 3]
mi_lista[0] = 0

lista = list(mi_tupla)
tupla = tuple(lista)
print(lista)
print(2 in lista)

print(tupla.count(1))
print(len(mi_tupla))

tupla_unitaria=("Xan",)
print(len(tupla_unitaria))

otra_tupla = "Fecha", 12, 3, 1995
print(otra_tupla)
nombre, dia, mes, ano = otra_tupla

# mi_tupla[0]= 0 # TypeError: 'tuple' object does not support item assignment
print type(mi_tupla)