## PARTE 1

miTuple = (1,2,3,4)


print(type(miTuple)) # Imprimir tipo de dato

print(miTuple[3]) # En este caso la ubicacion se da de manera negativa y de izquierda a derecha, en este caso nos da 1, pero también se puede indezar tal cual las posiciones de un array

## PARTE 2

miTuple = (1,2,(10,20),4)
print(miTuple[-2])
print(miTuple[2][0])


## PARTE 3
miTuple = (1,2,(10,20),4)

    #     ## Casteo de tuple a list y viceversa
miTuple = list(miTuple)
print(type(miTuple))

miTuple = tuple(miTuple)
print(type(miTuple))

## PARTE 4

t = (1,2,3)
x, y, z = t ## Se puede asignar de manera automática siempre y cuando la cantidad de variables sean iguales a la cantidad de elementos de la lista, diccionario o tuple


print(x, y, z)

##PARTE 5
    ## Imprimir cantidad de elementos
t = (1,2,3,1)

print(len(t))

    ## Imprimir cantidad de elementos iguales, en este caso el valor a contar sería uno, por lo que el resultado sería 2

print(t.count(1))

    ## Consultar el número del índice o posición de un elemento
print(t.index(2))


## EJERCICIOS

    # ## 1
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))
    
    # ## 2
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

    # ## 3
mi_tupla = (1, 2, 3, 4)
a, b, c, d = mi_tupla
    
