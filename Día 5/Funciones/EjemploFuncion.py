## Obtener el precio mayor de una lista de cafes
def cafeMasCaro(listaPreciosCafe):
    precioMayor = 0
    cafeCaro = ""

    for cafe, precio in listaPreciosCafe:
        if precio > precioMayor:
            precioMayor = precio
            cafeCaro = cafe
        
        else:
            pass

    return(precioMayor, cafeCaro)


precios_cafe = [('Capuchino', 1.5), ('Expresso', 4.7), ('Moka', 1.9)] ## Lista de tuples

precio, cafe = cafeMasCaro(precios_cafe)

print(f'El cafe más caro es: {cafe} cuyo precio es {precio}')
