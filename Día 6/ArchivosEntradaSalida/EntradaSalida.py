## La ruta donde se ejecuta generalmente es la carpeta raíz de todo el proyecto, en este caso PythonCourse, por lo que la ruta del archivo tendrá que continuar con el path desde la carpeta raíz

miArchivo = open('Día 6\ARCHIVOS PARA LA PRACTICA\Prueba.txt')

## Leer Todo
#print(miArchivo.read())

## Leer la primera linea
#print(miArchivo.readline())

## Con ReadLine también se puede leer todo el archivo pero sobreescribiendo una variable
## En ejecucion se muestra un salto de linea, eso se puede evitar con la función rstrip() -> Siempre y cuando sea necesario
## Se pueden aplicar todos los métodos para un string.
unaLinea = miArchivo.readline()
print(unaLinea.rstrip())

unaLinea = miArchivo.readline()
print(unaLinea.rstrip())

unaLinea = miArchivo.readline()
print(unaLinea.rstrip())

miArchivo.close()

## PARTE 2

## Al usar readlines, cada linea se convierte en un elemento de una lista
## Si el archivo ya fue leído anteriormente, no mostrará nada, se tendría que cerrar la primera lectura, en este caso la primera lectura se realiza desde la linea 14 hasta la 21.
miArchivoLista = open('Día 6\ARCHIVOS PARA LA PRACTICA\Prueba.txt')

todas = miArchivoLista.readlines()

print(todas)

## Tener en cuenta que el tiempo de ejecucion varía según el tamaño de los archivos que se abren

## UN ARCHIVO SIEMPRE SE TIENE QUE CERRAR
miArchivoLista.close()