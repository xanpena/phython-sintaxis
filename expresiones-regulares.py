import re

cadena = "ExprimIendo lAs exPrEsiones regulares en en PythOn."

busqueda = "regulares"

if re.search(busqueda, cadena) is not None:
    print("Texto encontrado!")
else:
    print('Texto no encontrado')


texto = re.search(busqueda, cadena)

print("Inicio de la coincidencia", texto.start())
print("Final de la coincidencia", texto.end())
print("Final de la coincidencia", texto.span())

print(len(re.findall('en', cadena)))
print(len(re.findall(' en ', cadena)))
print('#---------------------------------------')
# ---

nombres = ['Ana García', 'Luis Iglesias', 'Pedro Flores', 'Martín Martínez', 'Gonzalo Gonzalez', 'Fuencis Fuentes', 'Ana Iglesias']

for nombre in nombres:
    if re.findall('^Ana', nombre): # Que empiezan por
        print(nombre)

    if re.findall('es$', nombre): # Que finalicen por
        print(nombre)

    if re.findall('[z]', nombre): # Encuentra la letra z
        print(nombre)

    if re.findall('[ií]', nombre): # Busca i acentuada e i sin acentuar
        print(nombre)

    if re.findall('[o-t]$', nombre): # Muestra todos los nombres que terminen por una letra entre la o y la t
        print(nombre)
print('#---------------------------------------')
# --- match y search

# match busca coincidencias en un patrón de búsqueda al comienzo de una cadena de texto

nombre1 = "Sandra López"
nombre2 = "Antonio Gómez"
nombre3 = "sandra López"

if re.match("Sandra", nombre1):
    print('Nombre encontrado')
else:
    print('Nombre no encontrado')

if re.match("Sandra", nombre3):
    print('Nombre encontrado')
else:
    print('Nombre no encontrado')

if re.match("Sandra", nombre3, re.IGNORECASE): 
    print('Nombre encontrado')
else:
    print('Nombre no encontrado')

if re.match("ópez", nombre3): # match siempre busca por el principio
    print('Nombre encontrado')
else:
    print('Nombre no encontrado')


if re.search("ópez", nombre3): # y search por el final
    print('Nombre encontrado')
else:
    print('Nombre no encontrado')