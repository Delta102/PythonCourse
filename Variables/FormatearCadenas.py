## Para poder contatenar una cadena de texto más otro tipo de dato diferente como en el archivo Conversiones.py a str se tiene que formatear toda la cadena
    ## PARTE 1
x = 10
y = 5

print("Mis numeros son: "+ str(x) + " y " + str(y))

        # ## COMANDO FORMAT 1.0
print("La suma de los números {} y {} es igual a {}".format(x,y,x+y))


    ## PARTE 2
color = "rojo"
matricula = 541926
        ## COMANDO FORMAT 2.0
print(f"El auto es {color} y su matricula es {matricula}")

## PRÁCTICA FORMATEAR CADENAS
    ## 1
nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058

print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

    ## 2
puntos_nuevos = 350
puntos_totales = 1225

print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")

    ## 3

puntos_anteriores = 875
puntos_nuevos = 350

print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_anteriores+puntos_nuevos} puntos")