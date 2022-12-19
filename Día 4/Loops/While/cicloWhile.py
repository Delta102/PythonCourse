monedas = 5
while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo más dinero")


## PARTE 2

respuesta = "s"
while respuesta == "s":
    respuesta = input("Quieres seguir? (s/n): ")
else:
    print("Gracias")

## PARTE 3

    ## PASS
respuesta = "s"
while respuesta == "s":
    print("asd")
    pass
    print("Hola")


    ## BREAK

nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'r': 
        break
    print(letra)

    ## CONTINUE
nombre = input("Tu nombre: ")
for letra in nombre:
    if letra == 'r': 
        continue
    print(letra)