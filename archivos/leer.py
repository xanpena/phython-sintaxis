# -+- coding: utf-8 -*-

def run():
    with open('numeros.txt') as f:
        #print(f.realines())
        for line in f:
            print(line)
            #line.count('hacia')

    #try:
    #    f = open()
    #finally:
    #    f.close()

if __name__ == '__main__':
    run()