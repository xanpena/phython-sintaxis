# -+- coding: utf-8 -*-

# 5! = 5*4*3*2*1

def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number -1)

if __name__ == '__main__':
    number = int(input('Escribe un numero: '))
    result = factorial(number)
    print('El factorial de {} es {}'.format(number, result))