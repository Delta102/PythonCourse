## CONVERSIONES IMPLÍCITAS
    ##PARTE 1
    # Python convierte los tipos de una variable de manera automática. Por ejemplo "num1" inicialmente es de tipo INT; luego de sumarlo con num2, este se convierte a un tipo de dato
num1 = 20
num2 = 30.5

num1 += num2

print(num1)

print(type(num1))
print(type(num2))



## CONVERSIONES EXPLÍCITAS
    ## PARTE 2
    # Como programadores le podemos pedir que Python cambie el tipo de dato de una variable de manera manual

num1 = 5.8
print(num1)
print(type(num1))

num2 = int(num1)        ## Con esta sentencia podemos realizar la conversión del tipo de dato
print(num2)
print(type(num2))

edad = input("Dime tu edad: ")
print(type(edad))

edad = int(edad)
print(type(edad))

nueva_edad = 1 + edad

print("Tu nueva edad es: "+nueva_edad)

## PRÁCTICA CON CONVERSIONES
    ## 1
num1 = 7.5
print(type(int(num1)))

    ## 2
num2 = 10
print(type(float(num2)))

    ## 3

num1 = "7.5"
num2 = "10"

print(float(num1) + int(num2))