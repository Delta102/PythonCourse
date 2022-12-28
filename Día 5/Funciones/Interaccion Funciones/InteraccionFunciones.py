from random import shuffle

palitos = ['-', '--', '---', '----']

# Mezclar palitos
# Manera con la libreria
shuffle(palitos)

# Con funcion: 
def mezclar(lista):
    shuffle(lista)
    return lista

## Pedirle intento

def probarSuerte():
    intento = ''
    while(intento not in ['1','2','3','4']):
        intento = input("Elige un número del 1 al 4: ")

    return int(intento)


## Comprobar Intento Si el intento del usuario es equivalente al palito elegido

def comprobarIntento(lista, intento):
    if(lista[intento - 1] == '-'):
        print("A lavar los platos")
    
    else:
        print("Esta vez te has salvado")

    print(f"Te ha tocado {lista[intento-1]}")


palitosMezclados = mezclar(palitos)
seleccion = probarSuerte()

comprobarIntento(palitosMezclados, seleccion)