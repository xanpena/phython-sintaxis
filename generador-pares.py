def generaPares(limite):
    num = 1

    while num < limite:
        yield num * 2

        num=num+1

devuelvePares = generaPares(100)

for i in devuelvePares:
    print(i)