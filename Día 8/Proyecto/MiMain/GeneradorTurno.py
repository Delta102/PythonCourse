import os

def generarTurno(letra):
    for turno in range(0,10000000):
        match letra:
            case 'P':
                yield f"{letra} - {turno}"
            case 'F':
                yield f"{letra} - {turno}"
            case 'C':
                yield f"{letra} - {turno}"

p = generarTurno('P')
f = generarTurno('F')
c = generarTurno('C')

def verificarOpciones(opcion):
    match opcion:
        case 1:
            os.system('CLS')
            print('<<-- PERFUMERIA -->>')
            print("Su turno es: ")
            print(next(p))
            os.system('pause')
            os.system('cls')

        case 2:
            os.system('CLS')
            print('<<-- FARMACIA -->>')
            print("Su turno es: ")
            print(next(f))
            os.system('pause')
            os.system('cls')

        case 3:
            os.system('CLS')
            print('<<-- COSMÉTICOS -->>')
            print("Su turno es: ")
            print(next(c))
            os.system('pause')
            os.system('cls')
        
        case _:
            print("SALIENDO....")