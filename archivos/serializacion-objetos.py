import pickle

class Coche:
    """ Abstracción del objeto coche."""
    def __init__(self, gasolina):
        self.gasolina = gasolina
        print("Tenemos", gasolina, "litros")

    
    def arrancar(self):
        if self.gasolina > 0:
            print("Arranca")
        else:
            print("No arranca")


    def conducir(self):
        if self.gasolina > 0:
            self.gasolina -= 1
            print("Quedan", self.gasolina, "litros")
        else:
            print("No se mueve")


coche1 = Coche(50)
coche2 = Coche(20)
coche3 = Coche(3)

coches = [coche1, coche2, coche3]

# volcamos la información
fichero = open("binario-coches", "wb")
pickle.dump(coches, fichero)
fichero.close()
del(fichero)

# accedemos a la información
fichero=open('binario-coches', 'rb')
miscoches = pickle.load(fichero)
fichero.close()

for c in miscoches:
    c.arrancar()