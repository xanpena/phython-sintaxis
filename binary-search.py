# -+- coding: utf-8 -*-

def binary_search(numbers, number_to_find, low, high):

    mid = (low + high) / 2

    if low > high:
        return False

    if numbers[mid] == number_to_find:
        return True
 
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)


if __name__ == '__main__':
    numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 49, 51]

    number_to_find = int(input('Ingresa un numero:'))

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)

    if result is True:
        print(u'El numero está en la lista')
    else:
        print(u'El numero no está en la lista')