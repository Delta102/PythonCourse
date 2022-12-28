## 1

    # Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada lista_numeros con valores positivos y negativos.

    # No invoques la función, solo es necesario definirla.

lista_numeros = []

def todos_positivos(lista):
    for n in lista:
        lista_numeros.append(n)
        if n < 0:
            return False
        else: 
            pass
    
    return True


## 2

    # Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.



def suma_menores(lista):
    temp = 0
    for numero in lista:
        if numero in range(0, 1000):
            temp += numero
        else:
            pass

    return temp

lista_numeros = [55, 150, 120, 5000000]

result = suma_menores(lista_numeros)
print(result)


## 3

    # Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.

def cantidad_pares(lista_numeros):
    temp = []
    for n in lista_numeros:
        if(n % 2 == 0):
            temp.append(n)
        else:
            pass
    
    return len(temp)

lista_numeros = [55,10,35,40]
