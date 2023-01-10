def suma():
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))

    print(n1 + n2)
    print("Gracias por sumar")

try:
    ## Código que queremos probar
    suma()
except:
    ## Código a ejecutar si hay un error
    print("Algo no ha salido bien!!")
else:
    ## Código a ejecutar si no hay un error
    print("Hiciste todo bien")
finally:
    ## Código que se ejecutará de todos modos
    print("Eso fue todo")


##PARTE 2
##### TIPOS DE ERRORES
## En el caso de que un usuario ingrese un string se mostrará el error :ValueError
## Ejemplo: En la concatenación entre un string y un integer, se mostrará el error: TypeError
## Todo esto se puede controlar con try


def suma2():
    n1 = int(input("Número 1: "))
    n2 = int(input("Número 2: "))

    print(n1 + n2)
    print("Gracias por sumar" + n1) ## Esta parte dará un error de tipo: TypeError

try:
    suma2() ## Esta parte dará un error de tipo: TypeError
except TypeError:
    print("Estás intentando concatenar tipos distintos")
except ValueError:  ## Cuando se ingresa dos datos con tipos diferentes, en este caso si el usuario ingresa una letra en lugar de numero para la función suma
    print("Ese no es un número")
else:
    print("Hiciste todo bien")
finally:
    print("Eso fue todo")


## PARTE 3
def pedirNumero():
    while True:
        try:
            numero = int(input("Dame un número: "))
        except:
            print("Ese no es un número")
        else:
            print(f"Ingresaste el numero {numero}")
            break

    print("Gracias")

pedirNumero()