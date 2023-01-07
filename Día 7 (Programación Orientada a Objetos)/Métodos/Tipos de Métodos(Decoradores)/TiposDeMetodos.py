##### MÉTODOS DE INSTANCIA
class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):

        print(f"Pio, mi color es {self.color}")
    
    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros")
        ## Podemos llamar a otros métodos dentro de métodos
        self.piar()

    def pintarNegro(self):
        ## Se puede cambiar los valores de los atributos
        self.color = "Negro"
        print(f"Ahora el pájaro es {self.color}")


## Instancia de clase
piolin = Pajaro('amarillo', 'canario')
piolin.pintarNegro()
piolin.volar(50)

## Se puede modificar el estado de la clase
piolin.alas = False

########### MÉTODOS DE CLASE
class Pajaro2:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):

        print(f"Pio, mi color es {self.color}")
    
    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros")
        self.piar()

    def pintarNegro(self):
        self.color = "Negro"
        print(f"Ahora el pájaro es {self.color}")

    ## Métodos de clase
    @classmethod
    def ponerHuevos(cls, cantidad):
        ## No es posible acceder a los atributos a través de Self
        print(f'Puso {cantidad} huevos')
        ## Para acceder a su atributo se usa lo siguiente:
        cls.alas = False    ## Cambio de valores
        print(Pajaro.alas)  ## Acceso a los atributos

    @staticmethod
    ## Los métodos no pueden acceder a las instancias, no se puede acceder ni modificar los atributos de la clase
    def mirar():
        print("El pájaro mira")

## EJECUCIÓN
## Los métodos de clase no necesitan de una instancia de objeto para poder ejecutarse
Pajaro2.ponerHuevos(3)
Pajaro2.mirar()


