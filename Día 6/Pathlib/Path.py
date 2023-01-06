from pathlib import Path

guia = Path("Barcelona", "SagradaFamilia")  ## Construye un formato de rutas dependiendo del sistema operativo
print(guia)

## Obtener ruta principal del usuario del sistema operativo actual
base = Path.home()
print(base)

guia = Path(base, "Barcelona", "SagradaFamilia.txt")    ## Permite concatenar para el formato de rutas
print(guia)

## CONCATENACION

guia = Path(base, "Europa", "España", Path("Barcelona", "SagradaFamilia.txt"))  ## Se puede concatenar para el sistema de rutas

print(guia)

## PARTE 2

guia2 = guia.with_name("LaPedrera.txt")
print(guia2)

## Parent devuelve el contenedor que contiene al último parámetro

print(guia.parent)  ## Devuelve Barcelona
print(guia.parent.parent)   ## Devuelve España

## Path nos permite enumerar los archivos y/o carpetas

guia3 = Path(Path.home(), "Download")
for txt in Path(guia).glob("*.exe"):    ## Nos devuelve la cantidad de elementos que terminan en la extensión específicada
    print(txt)

## Ver archivos dentro de alguna carpeta
guia4 = Path("Europa", "España", "Barcelona", "SagradaFamilia")
enEuropa = guia.relative_to(Path("Europa"))
inSpain = guia.relative_to("Europa", "España")

print(enEuropa) ## Ver el contenido de la carpeta Europa
print(inSpain)  ## Ver el contenido de la carpeta España