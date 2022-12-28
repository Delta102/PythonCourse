## Devolver boolean si mi numero se encuentra dentro de cierto rango
def chequear3Cifras(numero):
    return numero in range(100, 10000)


suma = 586+402

resultado = chequear3Cifras(suma)
print(resultado)

## Devolver boolean si en mi lista existe números de 3 cifras

def revisarCifras(lista):
    for n in lista:
        if(n in range(100,1000)):
            return True
        else:
            pass

    return False



lista = [55, 99 , 6000]              
resultado = revisarCifras(lista)    ## Si no se cumple esto devuelve un objeto vacío debido al pass del bucle
print(resultado)


lista = [500, 45, 1500]
resultado = revisarCifras(lista)    ## Caso contrario me devuelve el valor esperado, en este caso un True

print(resultado)


## El segundo ejercicio pero esta vez almacenando los resultados en una lista

def revisarCifras(lista):

    newList = []

    for n in lista:
        if(n in range(100,1000)):
            newList.append(n)
        else:
            pass

    return newList


lista = revisarCifras([555,199,600])
print(lista)