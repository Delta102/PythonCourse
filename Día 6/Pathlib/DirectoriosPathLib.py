from pathlib import Path, PureWindowsPath

carpeta = Path("E:/Cursos Desarrollo/PythonCourse/Día 6/ARCHIVOS DE PRUEBA")    ## PERMITE EJECUCIÓN EN DIFERENTES SISTEMAS OPERATIVOS

archivo = carpeta / 'Prueba.txt'

miArchivo = open(archivo)
print(miArchivo.read())


## Su equivalente es el siguiente

carpeta2 = Path("E:/Cursos Desarrollo/PythonCourse/Día 6/ARCHIVOS DE PRUEBA/Prueba.txt")
print(carpeta2.read_text())
print(carpeta2.name) ## Devuelve el nombre completo del archivo
print(carpeta2.suffix)   ## Nos devuelve el tipo del archivo, en este caso es un .txt
print(carpeta2.stem)     ## Devuelve el nombre sin la extensión del archivo, en este caso "Prueba"

## Ejemplo: Caso de la existencia de un ARCHIVO

if not carpeta2.exists():
    print("La ruta no existe")
else:
    print("La ruta si existe")


## PUREWINDOWSPATH: Sirve para transformar una ruta en un directorio de windows

carpeta = Path("E:/Cursos Desarrollo/PythonCourse/Día 6/ARCHIVOS DE PRUEBA/Prueba.txt")

rutaWindows = PureWindowsPath(carpeta)

print(rutaWindows)