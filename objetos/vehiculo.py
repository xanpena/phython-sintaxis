class Vehiculo:
    name = ''
    kind = ''
    color = ''
    price = 10000.00
    _numero_serie = '0A5SDF52E2E2D12336W5J'

    def description(self):
        desc = "%s es un %s %s. Vale $%.2f" % (self.name, self.kind, self.color, self.price)
        return desc

car1 = Vehiculo()
car1.name = 'Ford'
car1.kind = 'Fiesta'
car1.color = 'rojo'

print(car1.description())