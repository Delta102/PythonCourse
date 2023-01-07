class Animal:
    ## Constructor
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print("Este animal ha nacido")
    
    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):
    ## Herencia Extendida
    ## Constructor con los valores heredados, en este caso, edad y color
    def __init__(self, edad, color, alturaVuelo):
        super().__init__(edad, color)       ## La función super(), solo funciona para los atributos heredados
        self.alturaVuelo = alturaVuelo

    def hablar(self):
        print("Pio")    ## Si dos métodos se llaman igual, el método de la clase que hereda, en este caso (Pajaro), los valores se sobreescriben
    
    def volar(self, metros):
        print(f"El pájaro vuela {metros} metros")

    
piolin = Pajaro(3, 'amarillo')
piolin.nacer()



