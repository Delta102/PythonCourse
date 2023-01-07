## En los métodos dentro de las clases, la palabra self como argumento es obligatoria

class Pajaro:
    ## Para atributos estáticos, se pueden asignar de la siguiente manera:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    ## Ejemplo de método en clase
    def piar(self):
        ## Para acceder a los atributos dentro de un método se usa la palabra clave "self"
        print("Pio, mi color es {}".format(self.color))    ## Se puede llamar a los demás atributos de la siguiente manera  
    
    ## Método que recibe parámetros
    def volar(self, metros):
        print(f"El pájaro ha volado {metros} metros")


## Instancia de clase
piolin = Pajaro('amarillo', 'canario')

## Los métodos si llevan paréntesis
piolin.piar()
piolin.volar(50)