from random import *  ##Importación de librerías

aleatorio = randint(1,50)
print(aleatorio)

aleatorio = round(uniform(1,5),1)        ## DECIMALES
print(aleatorio)

aleatorio = random()    ## Genera un float aleatorio en el 0 y 1
print(aleatorio)

colores = ['azul', 'rojo', 'verde', 'amarillo']
aleatorio = choice(colores)
print(aleatorio)

numeros = list(range(5,51,5))
shuffle(numeros)

print(numeros)