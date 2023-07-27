class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        return 'Hola {} tienes {} años'.format(self.name, self.age)


if __name__ == '__main__':
    person = Person('Xan', 32)
    print (person.name)
    print (person.say_hello())