class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print('Ja ja ja')

    def hablar(self):       
        print("Qué tal?")   ## Si hay dos funciones que se llaman igual, dependiendo de la instancia, el resultado será según el orden indicado

class Hijo(Padre, Madre):    ## En los parámetros se puede colocar tantas clases como sea necesario. Además, la clase Hijo heredó primero la clase Padre y luego la clase Madre
    pass

class Nieto(Hijo):
    pass

miNieto = Nieto()
miNieto.hablar()
## Usando el método de la clase Madre
miNieto.reir()

print(Nieto.__mro__)    ## Nos indica el orden de la ejecución de la clase que hereda