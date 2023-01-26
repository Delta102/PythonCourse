## EXTRAER EL TÍTULO DE LA PÁGINA
import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/')

# print(resultado.text)   ## ESTO DEVUELVE TODO EL CÓDIGO FUENTE DE LA PÁGINA

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

# print(sopa) ## También devuelve todo el código fuente

# print(sopa.select('title'))    ## Imprimir todos los elementos que tengan la etiqueta indicada, incluyendo su css, en este caso <head> </head>, ## Además esto imprime como resultado una lista

## RECUPERAR SOLO EL TÍTULO DE LA PÁGINA(sin etiquetas)
print(sopa.select('title')[0].getText())


## EXTRAER UNA CLASE CSS COMPLETA DE UNA PÁGINA
# Se usa los selectores css, id = #, class = ., etc
resultadoClase = sopa.select('.replaced h1')   # Obtener todo lo que se encuentra dentro de la clase, En este caso se obtiene todos los h1 que se encuentran dentro de la clase replaced. Esto devuelve una lista

print(resultadoClase)

for elemento in resultadoClase:
    print(elemento.getText())


#### EXTRAER IMÁGENES

buscarImagen = requests.get('https://www.escueladirecta.com/courses')
sopa2 = bs4.BeautifulSoup(buscarImagen.text, 'lxml')

imagenes = sopa2.select('.course-box-image')[0]['src']    ## En este ejemplo, según el sistema web solo algunas imagenes cuentan con la clase sourse-box-image, es por eso que la búsqueda se realiza por clase TENIENDO EN CUENTA EL INDEX, SOLO ESTAMOS TOMANDO LA PRIMERA IMAGEN

print(imagenes)

imagenCurso1 = requests.get(imagenes)       ## Obtenemos el archivo con la palabra .content usando la url de la imagen
#print(imagenCurso1.content)

f = open('miImagen.jpg', 'wb')  ## La palabra 'wb' significa: w = write; b = binary (Escribir binario), recordar que las rutas de los archivos pueden ser modificadas

f.write(imagenCurso1.content)
f.close()