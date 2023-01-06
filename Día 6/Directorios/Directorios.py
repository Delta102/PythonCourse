import os

ruta = os.getcwd()  ## Obtener el Directorio del trabajo actual

print(ruta)

ruta = os.chdir('E:\\Cursos Desarrollo\\PythonCourse\\Día 6\\ARCHIVOS DE PRUEBA')   ## Nos permite establecer una ruta diferente al proyecto actual 

archivo = open('OtroArchivo.txt')
print(archivo.read())

archivo.close

## EL MODULO OS TAMBIÉN NOS PERMITE LA CREACIÓN DE CARPETAS
# ruta = os.makedirs('E:\\Cursos Desarrollo\\PythonCourse\\Día 6\\ARCHIVOS DE PRUEBA\\OTRA CARPETA')

## También se puede crear un archivo con el mismo comando

ruta = "E:\\Cursos Desarrollo\\PythonCourse\\Día 6\\ARCHIVOS DE PRUEBA\\OTRA CARPETA\\OtraPrueba.txt"

rutaPrincipal = os.path.dirname(ruta)    ## Con esto obtenemos la ruta principal
elemento = os.path.basename(ruta)        ## Con esto se obtiene el nombre del archivo
print(rutaPrincipal)
print(elemento)

## Otra forma de hacer lo del bloque de las lineas 19 - 24
elemento = os.path.split(ruta)
print(elemento)

## ELIMINAR CARPETAS

os.rmdir("Aquí va la ruta")  ## ELIMINAR DIRECTORIO


