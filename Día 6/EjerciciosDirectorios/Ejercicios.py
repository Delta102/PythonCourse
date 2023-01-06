## 1
    # Crea una función llamada abrir_leer() que abra (open) un archivo indicado como parámetro, y devuelva su contenido (read).

def abrir_leer(pathArchive):
    miArchivo = open(pathArchive)

    return miArchivo.read()  

## 2
    # Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"

def sobreescribir(pathArchive):
    miArchivo = open(pathArchive, 'w')
    miArchivo.write("contenido eliminado")

## 3
    # Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". Finalmente, debe cerrar el archivo abierto.

def registro_error(rutaArchivo):
    miArchivo = open(rutaArchivo, 'a')
    miArchivo.write("se ha registrado un error de ejecución")
    miArchivo.close()
