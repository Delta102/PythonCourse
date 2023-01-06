from os import system

## Poner en el lugar donde quieres limpiar la consola

nombre = input("Dime tu nombre: ")
edad = input("Dime tu edad: ")

system('cls')       ## El comando cls solo funciona para usuarios de windows

print(f"Tu nombre es {nombre} y tienes {edad} años")

