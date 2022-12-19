x = True

if x:
    print("Es correcot")

if(5 == 2):
    print("Es correcto")
else:
    print("Incorrecto")

if (10>9):
    print("Es correcto")



### PARTE 2
mascota = "perros"
if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro' :
    print("Tienes un perro")
elif mascota == 'pez':
    print("Tienes un pez")
else:
    print("No sé que animal tienes")


### PARTE 3

edad = 16
calificacion = 9
if (edad < 18):
    print("Eres menor de edad")
    if(calificacion >= 7):
        print("Estás aprobado")
    else:
        print("Desaprobado")
else:
    print("Eres adulto")