class Persona():

    def __init__(self, nombre, edad, lugar):

        self.nombre = nombre
        self.edad = edad
        self.lugar = lugar

    def descripcion(self):

        print("Nombre: ", self.nombre, " Edad: ", self.edad, " Lugar: ", self.lugar)

class Empleado(Persona):

    def __init__(self, nombre_empleado, edad_empleado, lugar_empleado, sueldo, antiguedad):
        
        super().__init__(nombre_empleado, edad_empleado, lugar_empleado)

        self.sueldo = sueldo
        self.antiguedad = antiguedad

    def descripcion(self):

        super().descripcion()
        print("Sueldo: ", self.sueldo, "Antigüedad: ", self.antiguedad)
    
Antonio = Persona('Antonio', '54', 'Canarias')
Antonio.descripcion()

Miguel = Empleado('Miguel', '37', 'Valencia', '35.000', '12')
Miguel.descripcion()


print(isinstance(Miguel, Empleado))