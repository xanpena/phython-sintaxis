# -+- coding: utf-8 -*-

def run():
    with open('numeros.txt', 'wb') as f:
        for i in range(10):
            f.write(str(i))

    #try:
    #    f = open()
    #finally:
    #    f.close()

if __name__ == '__main__':
    run()