class Persona():
    def saludo_general(self):
        return "Hola Persona"

class Estudiante(Persona):
    
    
    def __init__(self, nombre, edad):
        super()
        self.nombre = nombre
        self.edad = edad

    
    def saludo(self):
        return "Hola %s " % self.nombre


e = Estudiante("Xan", 21)
print(e.saludo())
print(e.saludo_general())