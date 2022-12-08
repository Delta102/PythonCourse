## ARRAYS O VECTORES
miLista = ['a','b','c']
otraLista = ['hola', 55, 6.1]
lista3 = miLista + otraLista        # Puedo concatenar listas en otra lista
listaDesorden = ["g","o","b","m","c"]

print(miLista+otraLista)

    #     # A diferencia de los strings,  acá si se puede editar los elementos dentro de una lista

lista3.append('g') # Con la función append puedo agregar un elemento a la lista

lista3.pop()    # Con pop sin parámetros elimina el último elemento de un array

lista3.pop(0) # El parámetro es la posición del elemento

listaDesorden.sort()    # Con esta función puedo ordenar una lista desordenada
listaOrden = listaDesorden.sort()   # No se puede almacenar en otra variable, Esto devuelve NULL

listaDesorden.sort()
listaDesorden.reverse() # Con esta función se revierten los elementos de una lista
print(type(listaDesorden))

print(listaDesorden)

print(lista3)

resultado = len(miLista)    # Nos muestra la cantidad de elementos de la lista

resultado2 = miLista[0] # Indezación de un array, practicamente se puede aplicar los mismos métodos desarrollados en la clase de Strings



print(resultado)
print(type(miLista))

## PRÁCTICA CON ARRAYS
    ## 1
mi_lista = ["hola", 1, 2, True, "lista"]

    ## 2
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
    
    ## 3
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)