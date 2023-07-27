def numero_par(num):

    if num % 2 == 0:
        return True

numeros = [17, 23, 45, 89, 5, 4 , 65, 7, 95, 102]

print(list(filter(numero_par, numeros)))

#print(list(filter(lambda num: num%2==0, numeros)))