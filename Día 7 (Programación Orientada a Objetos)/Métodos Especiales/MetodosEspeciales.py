miLista = [1,1,1,1,1]

print(len(miLista))

class Objeto:
    pass

miObjeto = Objeto()

#print(len(miObjeto))    ## Error. Su solución se realiza en la linea 26
print(miObjeto)     ## Me indica el lugar en la memoria de la instancia



## PARTE 2

class CD:
    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    def __str__(self):
        return f"Album: {self.titulo} de {self.autor}"

    def __len__(self):
        return self.canciones

    def __del__(self):
        print("Se ha eliminado el CD")

    


miCD = CD('Avenged Sevenfold', 'Nightmare', 13)
print(miCD)

print(len(miCD))

## ELIMINAR INSTANCIA
del(miCD)   ## La instancia está eliminada, se puede modificar para que muestre un mensaje además de eliminar
