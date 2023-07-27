# -+- coding: utf-8 -*-

s = 'hola'
# s[0] = 'l' Error, los strings son inmutables
r = 'l' + s[1:]

print(s)
print(r)

# ASCII vs Unicode
# Python2 - Python3

string1 = 'ASCII por defecto ñ'
string2 = u'Prefijado con Unicode ñ'

print(string1)
print(string2)

print(string1[1:3])
print(string2[1:6:2]) #start:end:steps

#---

formato_numero_factura = ("Nº 0000-0", "-000 (ID: ", ")")
print("275".join(formato_numero_factura))


# -- Métodos de formato
cad = "hola, como estás?"
print(cad.capitalize()) # Hola, como estás?

cad = "Hola Mundo" 
print(cad.lower()) # hola mundo

cad = "hola mundo"
print(cad.upper()) # HOLA MUNDO

cad = "Hola Mundo"
print(cad.swapcase()) # hOLA mUNDO

cad = "hola mundo"
print(cad.title()) # Hola Mundo

print(cad.center(50)) # hola mundo                    

print(cad.center(50,"=")) # ====================hola mundo====================

print(cad.ljust(50,"=")) # hola mundo========================================

print(cad.rjust(50,"=")) # ========================================hola mundo

num = 123
print(str(num).zfill(12)) # 000000000123


# -- Métodos de búsqueda
cad = "bienvenido a mi aplicación"
cad.count("a") # 3
cad.count("a",16) # 2
cad.count("a",10,16) # 1
cad.find("mi") # 13
cad.find("hola") # -1
cad.rfind("a") # 21


# -- Métodos de validación
cad.startswith("b") # True
cad.startswith("m") # False
cad.startswith("m",13) # True
cad.endswith("ción") # True
cad.endswith("ción",0,10) # False
cad.endswith("nido",0,10) # True



