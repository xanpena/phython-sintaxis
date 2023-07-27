class Coche():
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enMarcha=False

    def arrancar(self):
        self.enMarcha = True

    def estado(self):
        if(self.enMarcha):
            return "El coche está en marcha"
        else:
            return "El coche está apagado"

miCoche = Coche()

print("El largo del coche es: ", miCoche.largoChasis)
print("El coche tiene ", miCoche.ruedas, " ruedas")

print(miCoche.estado())
miCoche.arrancar()
print(miCoche.estado())