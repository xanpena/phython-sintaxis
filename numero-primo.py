# -+- coding: utf-8 -*-

def is_prime(number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3, number):
            if(number % i == 0):
                return False
    return True


def run():
    print('C A L C U L A  S I  U N  N U M E R O  E S  P R I M O')
    print('----------------------------------------------------')
    number = int(input('Escribe un número: '))
    result = is_prime(number)

    if result is True:
        print('Es primo')
    else:
        print('No es primo')




if __name__ == '__main__':
    run()