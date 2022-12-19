nombres = ['Ana','Hugo', 'Valeria']
edades = [65,29,42, 50]

## Zip nos permite emparejar dos listas de manera ordenada, zip llega hasta el largo de la lista más corta, por ejemplo, el array de edades tiene 4 elementos, pero zip solo emparejará a 3 elementos por la cantidad de elementos que tiene la lista de nombres

combinados = list(zip(nombres, edades))
print(combinados)

## PARTE 2

nombres = ['Ana','Hugo', 'Valeria']
edades = [65,29,42, 50]
ciudades = ["Lima", "Cajamarca", "Córdova"]

combinados = list(zip(nombres, edades, ciudades))


for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} y vive en {ciudad}")