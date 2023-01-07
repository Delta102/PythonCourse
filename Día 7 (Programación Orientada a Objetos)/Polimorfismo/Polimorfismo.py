class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice muuu")
    
class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + " dice beee")
    

def animalHablar(animal):
    animal.hablar()


vaca1 = Vaca('Andrea')
oveja1 = Oveja("Nube")



animalHablar(vaca1)