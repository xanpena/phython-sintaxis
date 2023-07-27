# -+- coding: utf-8 -*-

palabra = "hola mundo"
tupla = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
lista = ("Marte", "Jupiter", "Urano", "Saturno")

print len(palabra)
print len(tupla)
print len(lista)
print range(20)
print len(range(20))
print sorted(lista)

import datetime
print type(datetime)
print type(datetime.datetime.now())
print type(3000000000000000000000000000000000000000000L)

print sum(tupla)

print round(3.1416, 2)

import math

print math.ceil(3.1416)
print math.floor(3.1416)
print dir(math)
#['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']


print map(str, [5, 3, 7])
print map(math.ceil, [5.4, 3.3, 7.8])