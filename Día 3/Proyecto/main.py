lista = []
print("<<<-- ANALIZADOR DE TEXTO -->>>")
print("-------------------------------")
print("\n")
text = input("1. Ingrese un texto: ")

print("-------------------------------")
print("Ahora, ingrese tres palabras: ")

lista.append(input("1. "))
lista.append(input("2. "))
lista.append(input("3. "))

print("<<<-- SOLUCIÓN -->>>")
print("1. ¿Cuántas veces aparece cada una de las letras que eligió?")

## Convertir texto a minúsculas para que se llegue a contar todo

text = text.lower()
resultado1 = text.count(lista[0])   # Cantidad de elementos iguales a lista[abc] encontradas en el texto
resultado2 = text.count(lista[1])
resultado3 = text.count(lista[2])

print(" a. La letra '"+lista[0] + "', aparece "+str(resultado1)+" veces en el texto")
print(" b. La letra '"+lista[1] + "', aparece "+str(resultado2)+" veces en el texto")
print(" c. La letra '"+lista[2] + "', aparece "+str(resultado3)+" veces en el texto")

print("-------------------------------")

print("2. ¿Cuántas palabras hay a lo largo de todo el texto?")
resultado4 = text.split()
print("   En su texto, hay " + str(len(resultado4)) + " palabras")

print("-------------------------------")
print("3. ¿Cuál es la primera letra del texto y cuál es la última")
print("   La primera letra es: "+text[0]+" y, la última letra es: "+text[len(text)-1]) ## Para la última letra también sirve text[-1]

print("-------------------------------")
print("4. Texto Invertido")
print(text[::-1])   ## Esto nos permite invertir una cadena de texto

resultado4.reverse()
print(' '.join(resultado4))   ## Nos permite invertir el orden de una de una cadena de texto usando el texto separado, en este caso el text.split(resultado4)

print("-------------------------------")
print("5. ¿La palabra 'Python' se encuentra en el texto?")
resultado5 = "python" in text
miDiccionario = {True:"sí", False:"no"}
print(f"La palabra 'Python' {miDiccionario[resultado5]} se encuentra en el texto ingresado")