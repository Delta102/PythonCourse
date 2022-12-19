lista = ['a','b','c','d']

for letra in lista:
    numeroLetra = lista.index(letra) + 1        ## Equivalente en c# a: lista[letra] o lista[i+1]
    print(f"Letra {numeroLetra}° = " + letra)

listaB = ["Pablo", "Laura", "Fede", "Luis", "Julia"]

for nombre in listaB:
    if(nombre.startswith('L')):             ## Con "startswith" podemos verificar que palabra empieza por la letra ubicada entre paréntesis
        print(nombre)


## PARTE 2

numeros = [1,2,3,4,5]
miValor = 0

for numero in numeros:
    miValor += numero

## PARTE 3

palabra = "python"

for letra in palabra:
    print(letra)

#### LA  PARTE 3 ES EQUIVALENTE A:

for letra in 'python':
    print(letra)

for objeto in [[1,2],[3,4],[5,6]]:
    print(objeto)                       ## Esto imprime cada par

for a, b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)        ##Esto imprime cada elemento



## PARTE 4

diccionario = {'clave1' : 'a', 'clave2' : 'b', 'clave3' : 'c'}

for item in diccionario:
    print(item)             ## Esto imprime las claves
    
for item in diccionario.items():
    print(item)             ## Esto imprime tanto la clave como su valor

for item in diccionario.values():
    print(item)             ## Esto imprime los valores