miSet = set((1,2,3,4,5)) ##En el set no puede haber más de un elemento repetido
print(miSet)

## Función Length
## Este tipo de funciones como len e in funciona para la mayoría de colecciones
print(len(miSet))

print(2 in miSet)

##PARTE 2

s1 = {1,2,3}
s2 = {3,4,5,2}

s3 = s1.union(s2) ## Unión de sets

print(s3)

##PARTE 3
x1 = {1,2,3}
x1.add(4)
x1.add(2);

x1.remove(4) ##Eliminación de elementos de un set
x1.discard(6)   ## No da error al tratar de eliminar un elemento inexistente

x1.pop() ## Elimina elemento aleatorio, se puede usar para sorteos

x1.clear() ## Vacía nuestro set

print(x1)