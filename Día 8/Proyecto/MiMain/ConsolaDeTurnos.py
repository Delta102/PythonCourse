from GeneradorTurno import *
import os




def inicio():
    os.system('cls')
    print("<<-- CONSOLA DE TURNOS -->>")
    opcion = 0
    while (opcion >= 0 and opcion < 4):
        print("-- ¿A qué área de atención desea dirigirse?")
        print("1. Perfumería:")
        print("2. Farmacia: ")
        print("3. Cosméticos: ")
        print("4. Salir")
        try:
            opcion = int(input("Eliga su opción: "))
        except ValueError:
            print("Opción inválida")
            print("Inténtelo nuevamente")
        else:
            verificarOpciones(opcion)

inicio()