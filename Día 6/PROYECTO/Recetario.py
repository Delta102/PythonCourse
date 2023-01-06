from pathlib import Path
from os import system
from shutil import rmtree
import os

def contarRecetasTotales(rutaCarpeta):
    listaCantidad = []
    for txt in Path(rutaCarpeta).glob("**/*.txt"):    ## Nos devuelve la cantidad de elementos que terminan en la extensión específicada
        listaCantidad.append(txt)

    return len(listaCantidad)

def verificarOpcion(opcion, rutaRecetas):
    opc = int(opcion)
    
    match opc:
        case 1:
            print("<<-- VER LAS RECETAS -->>")
            print("<< CATEGORÍAS DISPONIBLES >>")
            verCategoriaRecetas(rutaRecetas, 1, 0)
        case 2:
            print("<<-- CREAR RECETA -->>")
            print("<< CATEGORÍAS DISPONIBLES >>")
            verCategoriaRecetas(rutaRecetas, 2, 0)
        case 3:
            system('cls')
            print("<< CREAR NUEVA CATEGORÍA >>")
            nombreCategoria = input('Ingrese el nombre de la nueva categoría: ')
            crearCategoria(rutaRecetas, nombreCategoria)

        case 4:
            print("<<-- ELIMINAR RECETA -->>")
            print("<< CATEGORÍAS DISPONIBLES >>")
            verCategoriaRecetas(rutaRecetas, 1, 1)
        case 5:
            print("<<-- ELIMINAR CATEGORIA -->>")
            print("<< CATEGORÍAS DISPONIBLES >>")
            verCategoriaRecetas(rutaRecetas, 3, 0)
        
        case _:
            print("Saliendo.....")

## CRUD DE LAS RECETAS SEGÚN SU CATEGORÍA
def verCategoriaRecetas(ruta, verificador, identificadorOpc4):
    contenido = os.listdir(ruta)
    for posicion, carpeta in enumerate(contenido):
        print(f"{posicion+1}. {carpeta}")

    print("0. Regresar")
    categoriaOpcion = int(input("Elegir Opción: "))
    if categoriaOpcion == 0:
        menu()

    rutaTotal = Path(ruta, contenido[categoriaOpcion-1])

    if verificador == 1 and identificadorOpc4 == 0:
        verRecetasByCarpeta(rutaTotal, 0)
    elif verificador == 1 and identificadorOpc4 == 1:
        verRecetasByCarpeta(rutaTotal, 1)

    if verificador == 2:
        system('cls')
        print(f'<< CREAR NUEVA RECETA EN LA CATEGORÍA {contenido[categoriaOpcion-1].upper()}>>')
        crearReceta(rutaTotal)

    if verificador == 3:
        eliminarCategoria(rutaTotal)


def eliminarCategoria(ruta):
    rmtree(ruta)
    print("La categoría ha sido eliminada")

def crearCategoria(ruta, nombreCategoria):
    ruta = Path(ruta, nombreCategoria)
    os.mkdir(ruta)

    print("La categoría ha sido creada correctamente")



def crearReceta(ruta):
    nombreArchivo = input("Ingrese nombre del archivo: ")
    contenidoArchivo = input("Ingrese el contenido de su receta: ")
    nombreArchivo = nombreArchivo + ".txt"
    rutawithArchiveName = Path(ruta, nombreArchivo)

    miReceta = open(rutawithArchiveName, "w")
    miReceta.write(contenidoArchivo)
    miReceta.close()

    print("Su receta ha sido creada correctamente")


def verRecetasByCarpeta(ruta, identificadirOpc):
    system('cls')

    print("<< RECETAS DISPONIBLES >>")

    contenido = os.listdir(ruta)
    for posicion, archivo in enumerate(contenido):
        print(f"{posicion+1}. {archivo}")
    
    recetaOpcion = int(input("Elegir Receta: "))
    rutaTotal = Path(ruta, contenido[recetaOpcion-1])
    if identificadirOpc == 0:
        abrirReceta(rutaTotal)
    elif identificadirOpc == 1:
        eliminarReceta(rutaTotal)

def eliminarReceta(ruta):
    os.remove(ruta)
    print("La receta ha sido eliminada correctamente")

def abrirReceta(ruta):
    miReceta = open(ruta)
    print(miReceta.read())
    miReceta.close()
    system('PAUSE')
    system('cls')
    
def rutaBaseRecetas():
    rutaBase = Path(Path.home())
    ruta = Path(rutaBase, "Downloads", "Recetas")
    return ruta


## INICIO
system('cls')
print('''Bienvenido Usuario
La ruta de acceso al directorio en donde se encuentra la carpeta de recetas es la siguiente:''')
rutaRecetas = rutaBaseRecetas()
print(rutaRecetas)

## CANTIDAD DE RECETAS
cantidadRecetas = contarRecetasTotales(rutaRecetas)
print("")
print(f'En esta carpeta se encuentran {cantidadRecetas} recetas')

system('pause')
system('cls')

system('cls')
print("!---- A CONTINUACIÓN SE LE MOSTRARÁ LAS SIGUIENTES OPCIONES ----¡")
print("Elija cualquier opción: ")
opcion = 0
while(opcion!=6):
    print("1. Elegir categoría de recetas")
    print("2. Crear Nueva receta en la categoría deseada")
    print("3. Crear Nueva Categoría")
    print("4. Eliminar Recetas")
    print("5. Eliminar Categoría")
    print("6. Salir")
    opcion = input("Ingresar Opcion: ")
    opcion = int(opcion)
    ## SWITH DE OPCIONES
    system('cls')
    verificarOpcion(opcion, rutaRecetas)