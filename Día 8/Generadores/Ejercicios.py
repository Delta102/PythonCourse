## 1
    # Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números, iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next.

def miGenerador():
    x = 0
    while True:
        x += 1
        yield x

generador = miGenerador()


## 2
    # Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7, iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).

def miGenerador():
    x = 0
    while True:
        x += 7
        yield x

generador = miGenerador()


## 3
    # Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea llamado:

    # "Te quedan 3 vidas"

    # "Te quedan 2 vidas"

    # "Te queda 1 vida"

    # "Game Over"

    # Almacena el generador en la variable perder_vida

def misVidas():
    vidas = 3
    yield f"Te quedan {vidas} vidas"

    vidas -= 1
    yield f"Te quedan {vidas} vidas"

    vidas -= 1
    yield f"Te quedan {vidas} vida"

    vidas -= 1
    yield "Game Over"

perder_vida = misVidas()
