## https://books.toscrape.com/catalogue/page-2.html

import bs4, requests
# Podemos cambiar el valor numérico por un valor string literal de las páginas para poder hacer algo iterable, en este caso usaremos "{}"
baseUrl = 'https://books.toscrape.com/catalogue/page-{}.html'

# for n in range(1, 11):
#     print(baseUrl.format(n))    ## Esto quiere decir que la URL contendrá todas las páginas desde el 1 a la 10

resultado = requests.get(baseUrl.format('1'))
sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

libros = sopa.select('.product_pod')  ## En el ejemplo vamos a capturar todos los libros incluyendo título y calificación

#ejemplo = libros[0].select('.star-rating.Three')    ## En la selección los espacios son reemplazados por un punto, ejem: '.star-rating Three' = '.star-rating.Three'
#print(ejemplo)

## Obtener el título del libro 1
ejemplo = libros[0].select('a')[1]['title']
print(ejemplo)