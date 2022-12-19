palabra = 'python'

lista = []

for letra in palabra:
    lista.append(letra)

## ESTO ES EQUIVALENTE A: 

lista = [letra for letra in palabra]
print(lista)

## EJEMPLO:

## QUIERO QUE MI LISTA ESTÉ COMPUESTO POR LOS NÚMEROS QUE ESTÉN DENTRO DEL RANGO DESDE 0 HASTA 20

lista = [n for n in range(0,21)]

## MI LISTA ESTÉ COMPUESTO POR CADA NÚMERO DIVIDIDO ENTRE 2 EN EL RANGO DE 0 A 20 Y QUE SU MULTIPLICACION POR 2 SEA MAYOR A 10

lista = [n/2 if n/2*2 > 10 else "No" for n in range(0,21)]
print(lista)

## EJEMPLO 2

## MEDIDA EN PIES
## Convertir los valores de la lista de pies a metros en una nueva lista
pies = [10,20,30,40,50]
metros = []

metros = [n*0.3048 for n in pies]

print(metros)