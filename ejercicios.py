# ------
# LISTAS
# ------

# 1. Lee por teclado números y guardalo en una lista, el proceso finaliza cuando metamos un número negativo. Muestra el máximo de los números guardado en la lista, muestra los números pares.

num=int(input("Número:"))
lista=[]
while num>0:
    lista.append(num)
    num=int(input("Número:"))        
print("Máximo: %d" % max(lista))
for n in lista:
    if n % 2 ==0:
        print(n,end=" ")
print()

# con list comprehension
for n in [x for x in lista if x % 2 == 0]:
    print(n)

# ---------------------------------------------------------------
# 2. Realizar un programa que, dada una lista, devuelva una nueva lista cuyo contenido sea igual a la original pero invertida. Así, dada la lista [‘Di’, ‘buen’, ‘día’, ‘a’, ‘papa’], deberá devolver [‘papa’, ‘a’, ‘día’, ‘buen’, ‘Di’].

lista=['Di', 'buen', 'dia', 'a', 'papa']
print(lista[::-1])

# ---------------------------------------------------------------
# 3. Dada una lista de cadenas, pide una cadenena por teclado e indica si está en la lista, indica cuantas veces aparece en la lista, lee otra cadena y sustituye la primera por la segunda en la lista, y por último borra la cadena de la lista

lista=['Di', 'buen', 'dia', 'a', 'papa',"hola","papa","buen","dia"]    
cadena=input("Cadena:")

if cadena in lista:
    print("La cadena está en la lista")
else:
    print("La cadena no está en la lista")    

print(lista.count(cadena))    
cadena2=input("Cadena a reemplazar:")
apariciones=lista.count(cadena)
pos=0

for i in range(0,apariciones):
    pos=lista.index(cadena,pos)
    lista[pos]=cadena2
print(lista)

# ---------------------------------------------------------------
# 4. Dado una lista, hacer un programa que indique si está ordenada o no.

lista=[2,3,4,1]
lista2=lista[:]
lista.sort()
if lista==lista2:
    print("Lista ordenada")
else:
    print("Lista no ordenada")


# ------
# BUCLES
# ------

# 1. Pedir un número por teclado y mostrar la tabla de multiplicar

# solución con while

numero = int(input("Número:"))
cont = 1
while (cont<11):
    print ("%d * %d = %d" % (cont, numero, cont * numero))
    cont += 1

# solución con for

numero = int(input("Número:"))
for cont in range(1,11):
    print ("%2d * %d = %2d" % (cont, numero, cont * numero))

# ---------------------------------------------------------------
# 2. Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se representa por el número seguido de un signo de exclamación. Por ejemplo 5! = 1x2x3x4x5=120

num=int(input("Número:"))
fact=1
for i in range(2,num+1):
    fact*=i
print("El resultado es %d" % fact)

# ---------------------------------------------------------------
# 3. Crea una aplicación que permita adivinar un número. En primer lugar la aplicación solicita un número entero por teclado. A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido. El programa termina cuando se acierta el número.

secreto=int(input("Número secreto:"))
num=int(input("Número:"))
while num!=secreto:
    if num>secreto:
        print("El número es menor")
    else:
        print("El número es mayor")
    num=int(input("Número:"))
print ("Has acertado")

# ---------------------------------------------------------------
# 4. Programa que muestre la tabla de multiplicar de los números 1,2,3,4 y 5.

for numero in range(1,6):
    for cont in range(1,11):
        print ("%2d * %d = %2d" % (cont, numero, cont * numero))
    print()

# ---------------------------------------------------------------
# 5. Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la unidad.

num=int(input("Número:"))
primo = True
for cont in range(2,num):
    if num%cont==0:
        primo=False
        break
if primo:
    print("Es primo")
else:
    print("No es primo")

