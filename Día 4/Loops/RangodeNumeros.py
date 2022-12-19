## Permite ejecución de n veces de una porción de código;
## Equivalencia C#:
    ## for (int i=0; i< 5; i++)
        ## Console.WriteLine(i);            //Imprime: 1 2 3 4 5

for numero in range(5):
    print(numero)

for numero in range(1, 5):
    print(numero)

for numero in range(20, 31, 3):     ## El tercer parámetro nos indica cada cuantos números se tomará en el for
    print(numero)

## PARTE 2

lista = list(range(1,101))  ## Se crea lista con los elementos desde el 1 HASTA EL 100

print(lista)