## PARTE 1
nombre = "Carina"
    #     #  nombre[0] = "K"     ## Un string no puede ser modificado, por eso esta línea da error
print(nombre)

## PARTE 2
n1 = "Kari"
n2 = "na"

print(n1 + n2)

    # # Multiplicación de string
print(n1 * 10)

    # ## PARTE 3
    # # De esta forma también se puede hacer saltos de línea
poema = """Mil pequeños peces blancos
    como si hirviera
    el color del agua"""

print(poema)

print("agua" in poema)      # Me indica si una palabra se encuentra dentro de la cadena de texto
print("agua" not in poema)      # Me indica si una palabra NO se encuentra dentro de la cadena de texto

print(len(poema))   # Me indica la cantidad de caracteres de la cadena de texto

## PRÁCTICA PROPIEDADES DE STRINGS
    ## 1
print("Repetición" * 15)

    ## 2
txt = """Tierra mojada
       mis recuerdos de viaje,
       entre las lluvias"""

print("agua" not in txt)

    ## 3
txt = "electroencefalografista"
print(len(txt))
