## PARTE 1
    ## Los diccionarios están compuestos por x número de pares, cada par está compuesto por una clave y un valor, tal cual como en la vida real.
    ## Por ejemplo en la línea 4 la clave es: 'c1' y su valor es 'valor1', la clave es única pero los valores pueden ser iguales para las claves
diccionario = {'c1': 'valor1', 'c2':'valor1'}

resultado = diccionario['c1'] ## -> En lugar de indicar la posición como en un array, la indezación es realizada por la clave del diccionario


## PARTE 2

cliente = {'nombre':'Juan', 'apellido' :'Fuentes', 'peso':88, 'talla':1.76 }
consulta = (cliente['apellido'])
print(consulta)

## PARTE 3

dic = {'c1':55, 'c2':[10,20,30], 'c3':{'s1':100, 's2':200}}
print(dic['c2'])    ## -> Como resultado me imprime la lista,
print(dic['c2'][2]) ## -> Me imprime la lista en la posicion 2

print(dic['c3']['s2'])  ## -> También me permite realizar la consulta en un diccionario dentro de otro diccionario

## PARTE 4

    # SUB EJERCICIO
        # Imprimir letra E en mayúscula según el diccionario

dic = {'c1':['a','b','c'], 'c2':['d','e','f']}
print(dic['c2'][1].upper())

## PARTE 5
    ## AGREGAR ELEMENTOS A DICCIONARIO YA CREADO

dic = {1:'a', 2:'b'}
print(dic)


dic[3] = 'c'

print(dic)

    ## SOBREESCRIBIR VALOR EXISTENTE


dic[2] = 'B'
print(dic)

    ## SABER LAS CLAVES DE UN DETERMINADO DICCIONARIO

print(dic.keys())

    ## SABER TODOS LOS VALORES DE UN DICCIONARIO

print(dic.values())

    ## SABER TODOS LOS ITEMS DE UN DICCIONARIO

print(dic.items())


## EJERCICIOS

    ##1
mi_dic = {'nombre':'Karen','apellido':'Jurgens','edad':35,'ocupacion':'Periodista'}

    ##2
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])

    ##3
mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}

mi_dic['nombre'] = 'Felix'
mi_dic['apellido'] = 'Peralta'
mi_dic['edad'] = 20
mi_dic['ocupacion'] = 'Programador'
mi_dic['pais'] = 'Perú'

print(mi_dic)