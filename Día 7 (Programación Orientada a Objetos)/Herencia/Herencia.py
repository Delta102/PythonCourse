class Animal:
    pass

class Pajaro(Animal):   ## Pajaro recibe los atributos de Animal
    pass

print(Pajaro.__bases__) ## Me indica de quién hereda, en este caso, Pajaro hereda de Animal
print(Animal.__subclasses__())    ## Me indica a que clase le está heredando sus atributos

## PARTE 2:
class Animal2:
    ## Constructor
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")

class Pajaro2(Animal2):
    pass

piolin = Pajaro2(2, "Rojo")  ## La clase Animal necesita los parámetros de edad y color los cuales son obligatorios según su constructor


piolin.nacer()  ## Puedo acceder a los métodos y atributos de la clase Animal desde una instancia de la clase Pájaro
print(piolin.color)
print(piolin.edad)