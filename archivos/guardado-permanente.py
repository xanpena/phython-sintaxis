import pickle

class Persona:

    def __init__(self, nombre, genero, edad):
        self.nombre = nombre
        self.genero = genero
        self.edad = edad
        print("Persona {} creada correctamente.".format(self.nombre))

    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.edad)


class ListaPersonas:

    personas=[]

    def __init__(self):
        fichero = open("ficheroExterno", "ab+")
        fichero.seek(0)

        try:
            self.personas=pickle.load(fichero)
            print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            del(fichero)

    def agregar(self, persona):
        self.personas.append(persona)

    def listar(self):
        for persona in self.personas:
            print(persona)

personas = ListaPersonas()
