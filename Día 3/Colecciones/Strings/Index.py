## MÉTODO INDEX()
miTexto = "Esta es una prueba"
resultado = miTexto[-4]

resultado = miTexto.index("a") ## El método index nos indica la posición del elemento

resultado2 = miTexto.index("a", 5,10) ## El segundo parámetro nos indica el inicio de la posición de la búsqueda; El tercer parámetro nos indica el final de la 
    #                                       ## búsqueda

resultado3 = miTexto.rindex()   ## Con rindex la búsqueda se inicia al contrario
print(resultado)

## PRÁCTICA MÉTODO INDEX()
    ## 1
palabra = "ordenador"
print(palabra[4])
    
    ## 2
frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son"
resultado = frase.index("práctica")
print(resultado)