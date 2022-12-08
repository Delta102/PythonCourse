texto = "Este es el texto de Federico"
## SEPARADOR
texto = "Este es el texto de Federico"

    # ## Upper
resultado = texto.upper()
print(resultado)

    # ## Lower
resultado = texto.lower()
print(resultado)

    # ## Split
resultado = texto.split() ## En este caso separa por espacios
print(resultado)

    # ## Split 2.0

resultado = texto.split("t") ## En este caso separa por el caracter "t"
print(resultado)

## UNIR
a = "Aprender"
b = "Python"
c = "es"
d = "genial"
e = " ".join([a,b,c,d]) ## Toma a todos los elementos que serán separados por el valor antes del .join

print(e)

## MÉTODO FIND
resultado = texto.find("g") ## Al contrario de index, esta función no arroja un error, sino arroja un valor -1

## MÉTODO REPLACE
resultado = texto.replace("Federico", "Felix")  ## El primer parámetro significa el texto a reemplazar y el segundo parámetro es el texto por 
    #                                                 # el cual se reemplazará

print(resultado)

## PRÁCTICA MÉTODOS STRING
    ## 1
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())

    ## 2
lista_palabras = ["La","legibilidad","cuenta."]
union = " ".join(lista_palabras)
print(union)

    ## 3
frase = "Si la implementación es difícil de explicar, puede que sea una mala idea"
resultado = frase.replace("difícil", "fácil").replace("mala","buena")
print(resultado)

