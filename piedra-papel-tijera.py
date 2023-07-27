# -*- coding:utf-8-*-
import time
from time import sleep
import random

sus = "-" * 35
depo = ["piedra", "papel", "tijera"]
while True:
    user = raw_input("piedra, papel o tijera: ")
    if user not in depo:
        print("No hagas trampa!")
        continue
    pc = random.choice(depo)
    sleep(2)
    print("La computadora elijio {}.".format(pc))

    if user == pc:
        print "Empate!"
    elif user == 'piedra' and pc == 'tijera':
        print "Ganaste!"
    elif user == 'papel' and pc == 'piedra':
        print "Ganaste!"
    elif user == 'tijera' and pc == 'papel':
        print "Ganaste!"
    else:
        print "Perdiste!"
    print sus
