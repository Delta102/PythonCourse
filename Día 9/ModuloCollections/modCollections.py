## PARTE 1

## VER NÚMEROS DUPLICADOS DE UN ARRAY
from collections import Counter

numeros = [8,6,9,5,4,5,5,5,8,7,4,5,4,4]
print(Counter(numeros)) ## Esta impresión me indica la cantidad de veces que se repita algún valor en una lista


## PARTE 2

from collections import defaultdict

miDic = defaultdict(lambda: 'nada') ## Lambda significa que si en un diccionario no encuentra el valor deseado, devuelve el valor designado, en este caso: 'nada'
miDic['uno'] = 'verde'
print(miDic['uno']) ## verde
print(miDic['dos']) ## nada
