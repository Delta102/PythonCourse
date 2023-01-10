def decorarSaludo(funcion):
    def otraFuncion(palabra):
        print("Hola")
        funcion(palabra)    ## Esta funcion recibida como parámetro tomará la función que esté decorada
        print("Adiós")
    return otraFuncion

@decorarSaludo              ## Esto sirve como una especie de concatenacion
def mayuscula(texto):
    print(texto.upper())

@decorarSaludo
def minusculas(texto):
    print(texto.lower())


## Llamado 
minusculas("Python")    ##Como la funcion cuenta con su decorador, el resultado será "Hola" "python" "Adiós"
mayuscula("python")     ##Como la funcion cuenta con su decorador, el resultado será "Hola" "PYTHON" "Adiós"

## Esto también es equivalente a: 
mayusculaDecorada = decorarSaludo(mayuscula)    ## el parámetro es el nombre de la función
mayusculaDecorada("hola")   ## RESULTADO = "HOLA"
