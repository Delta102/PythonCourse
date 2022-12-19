from random import randint

nombre = input("Ingrese su nombre: ")

secretNumber = randint(1, 100)

print(f"Bueno, {nombre}, he pensado un número entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número")

for i in range(1,9):
    valor = input(f"Ingrese el {i}° valor: ")
    valor = int(valor)
    if(valor not in range(1,101)):
        print(f"Ha elegido un número que no está permitido, le quedan {8-i} intentos")
    
    if (valor < secretNumber):
        print("Ha elegido un número menor al número secreto. Su respuesta es incorrecta")
        print(f"Le quedan {8-i} intentos")
    elif (valor > secretNumber):
        print("Ha elegido un número mayor al número secreto. Su respuesta es incorrecta")
        print(f"Le quedan {8-i} intentos")
    else:
        print(f"Ha ganado en el intento número {i}°. Felicitaciones!!!!!")
        break