def mayuscula(texto):
    print(texto.upper())



def minuscula(texto):
    print(texto.lower())


def unaFuncion(funcion):
    return funcion

## Decorador 
miFuncion = mayuscula
miFuncion("python")

## PARTE 2, INCLUYE A LA LINEA 10 Y 11
unaFuncion(mayuscula("probando"))

## PARTE 3

def cambiarLetras(tipo):
    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    else:
        return minuscula


## Ejemplo de uso

operacion = cambiarLetras('may')
## Ejecución. En este caso como mi operacion tiene su tipo may, se ejecutara las mayusculas
operacion('palabra')    ## RESULT = "PALABRA"