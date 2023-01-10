## Función que devuelva el número 4

#### FUNCIÓN NORMAL:
def miFuncion():
    return 4

def miGenerador():
    yield   4       


print(miFuncion())
print(miGenerador())    ## Me indica el espacio de memoria donde está guardado el resultado de la función

g = miGenerador()
print(next(g))

## PARTE 2

#### FUNCIÓN QUE DEVUELVA UNA LISTA DE NÚMEROS DEL 1 AL 4 MULTIPLICADO POR 10

## FUNCIÓN NORMAL
def miFuncion():
    lista = []
    for x in range(1,4):
        lista.append(x*10)

    return lista

## FUNCIÓN GENERADOR
## Esta función es más óptima a la función normal
def miGenerador():
    for x in range(1,5):
        yield x * 10


## Llamado
g = miGenerador()
print(next(g))  ## En este momento recién se genera el valor, es decir primero se imprimirá el 10, pero el resto de valores no existen en el espacio de memoria
print(next(g))  ## Imprime 20, pero el resto de valores no existen por el momento y así sucesivamente mientras haya valores 

## PARTE 3
def mi_generador():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

gen = mi_generador()

print(next(g))
print(next(g))
print(next(g))