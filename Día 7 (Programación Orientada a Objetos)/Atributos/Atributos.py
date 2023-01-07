## DEFINICION DE ATRIBUTOS
class Pajaro:
    ## CONSTRUCTOR
    ## INIT se establece los atributos necesarios
    def __init__(self, color):  ## Este es mi constructor para la asignación de atributos. El primer parámetro es obligatorio y los que le siguen son los atributos
        self.color = color ## El self.color es la creacion del atributo

    ## La palabra SELF nos indica la instancia de un objeto que será creado. Cumple la función del "this." en otros lenguajes 

## Instancia de clase
miPajaro = Pajaro("Negro") ## Debido al constructor, es obligatorio pasarle el parámetro

## Acceder a los atributos de las clases
## Los atributos no contienen paréntesis
print(miPajaro.color)
