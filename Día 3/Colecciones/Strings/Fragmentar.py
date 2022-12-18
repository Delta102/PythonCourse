## SUB-STRINGS
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]  ## Esta porción significa que nos extraerá todo lo que se encuentre dentro de la cadena de texto desde la posición 2 hasta la 5
print(fragmento)

fragmento2 = texto[2:10:2] ## El tercer factor significa la extracción de cada x caracteres

## PRÁCTICA SUB-STRINGS
    ## 1
frase = "Controlar la complejidad es la esencia de la programación"
print(frase[:9])
    
    ## 2
frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
resultado = frase[8::3]
print(resultado)
    
    ## 3
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(frase[::-1])