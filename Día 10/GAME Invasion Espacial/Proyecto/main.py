## SE USARÁ LA LIBRERÍA PYGAME
## pip install pygame --pre en la carpeta base

import pygame, random, math
from pygame import mixer
pygame.init()   ## Inicilización de pygame

pantalla = pygame.display.set_mode((800, 600))      ## Anchura y altura respectivamente en píxeles, inicialización de la pantalla

seEjecuta = True
## Loop para que la pantalla se muestre siempre

## RUTA DE ARCHIVOS, IMÁGENES, LOGO, ETC
ruta = "E:\Cursos Desarrollo\PythonCourse\Día 10\GAME Invasion Espacial\Proyecto\Resources"
## Titulo e ícono
pygame.display.set_caption("Invasión Espacial") ## TÍTULO

## AGREGAR MUSICA
mixer.music.load(ruta+"\MusicaFondo.mp3")
mixer.music.set_volume(0.5) ## El volumen va de 0 a 1
mixer.music.play(-1)

icono = pygame.image.load(ruta + "\ovni.png")## Para ícono es recomendable un PNG de 32 píxeles

pygame.display.set_icon(icono)  ## Inicialización de ícono

## FONDO DE PANTALLA
fondo = pygame.image.load(ruta + "\Fondo.jpg")

## VARIABLES DEL JUGADOR
imgJugador = pygame.image.load(ruta + "\cohete.png")
# Posición del Jugador
# MEDICIONES PARA QUE EL JUGADOR QUEDE EXACTAMENTE EN EL MEDIO:
    ## EJE X:
        # 1. 800(anchura)/2 = 400
        # 2. 400 - (mitad del jugador, en este caso tiene 64 pixeles de anchura. En este caso es 32) 32 = 368

    ## EJE Y:
        # Al límite del borde
        # 1. 600(altura) - (tamaño del jugador (64 pixeles)) 64 = 536
jugadorX = 368
jugadorY = 500  ## Un poco más alto
jugadorXCambio = 0

# VARIABLES del ENEMIGO
imgEnemigo = []
enemigoX = []
enemigoY = []
enemigoXCambio = []    ## Que el enemigo se mueva a la derecha
enemigoYCambio = []     ## Que el enemigo se mueva hacia abajo
cantidadEnemigos = 8

for enemy in range(cantidadEnemigos):
    imgEnemigo.append(pygame.image.load(ruta + "\enemigo.png"))
    enemigoX.append(random.randint(0, 736))
    enemigoY.append(random.randint(50, 200))
    enemigoXCambio.append(0.3)
    enemigoYCambio.append(50)

# VARIABLES de la BALA
imgBala = pygame.image.load(ruta + "\mibala.png")
balaX = 0
balaY = 500 ## Altura de la nave
balaXCambio = 0 ## No es necesario
balaYCambio = 3     ## Velocidad de la bala
balaVisible = False

## VARIABLE PUNTAJE
puntaje = 0
## MOSTRAR PUNTAJE
fuenteLetra = pygame.font.Font('freesansbold.ttf', 32)  ## Primer parámetro es el estilo de letra y el segundo el tamaño
# Posicion del texto
textoX = 10
textoY = 10


## TEXTO FINAL DEL JUEGO
fuenteFinal = pygame.font.Font('freesansbold.ttf', 40)

def textoFinal():
    miFuenteFinal = fuenteFinal.render("JUEGO TERMINADO", True, (255, 255, 255))
    pantalla.blit(miFuenteFinal, (60, 200))   ## 60 y 200 van para la posición del Texto

## Función mostrar Puntaje
def mostrarPuntaje(x, y):
    texto = fuenteLetra.render(f"Puntaje: {puntaje}", True, (255, 255, 255))    ## El primer parámetro es el texto, el segundo es antialiasing y el tercero es el color
    pantalla.blit(texto, (x,y))



# Esta función tiene que actualizarse constantemente, es decir, ejecutar desde el bucle del juego
def jugador(x, y):
    pantalla.blit(imgJugador, (x, y)) ## POSICIÓN DEL JUGADOR EN PANTALLA


## Función de enemigo
def enemigo(x, y, enemyIterator):
    pantalla.blit(imgEnemigo[enemyIterator], (x, y))

## Función de la bala
def dispararBala(x, y): ## Enviar valores de la nava (Que la bala aparezca en el medio de la nave)
    global balaVisible
    balaVisible = True
    pantalla.blit(imgBala, (x+16, y + 10))  ## Posición de la nave

## FUNCIÓN COLLIDERS
def hayColision(x1, y1, x2, y2):
    operacion1 = math.pow((x2 - x1), 2)
    operacion2 = math.pow((y2 - y1), 2)
    distancia = math.sqrt(operacion1 + operacion2)

    if distancia < 27:  ## El segundo valor depende del tamaño de las figuras
        return True
    else:
        return False



while seEjecuta:

    ## COLOR DE PANTALLA (TIENE QUE ESTAR DENTRO DEL BUCLE) (RGB)
    # pantalla.fill((205, 144, 228))

    pantalla.blit(fondo, (0,0))
    ## MOVIMIENTO


    ## Si se encuentra el evento de quit (Botón de X en la pantalla), se sale del loop
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            seEjecuta = False
        
        if evento.type == pygame.KEYDOWN:   ## KEYDOWN: Tecla presionada
            if evento.key == pygame.K_LEFT:
                jugadorXCambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugadorXCambio = 0.3
            
            ## Dispara bala:
            if evento.key == pygame.K_SPACE:
                sonidoDisparo = mixer.Sound(ruta + "\disparo.mp3")
                sonidoDisparo.play()
                if not balaVisible:
                    balaX = jugadorX
                    dispararBala(balaX, balaY)

        if evento.type == pygame.KEYUP:     ## KEYUP: Si el usuario suelta una tecla
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugadorXCambio = 0

        

    ## UbICACIÓN DEL JUGADOR
    jugadorX +=jugadorXCambio

    ## AGREGAR UN OBJETO DE ACUERDO A LAS COORDENADAS (ESQUINA SUPERIOR IZQUIERDA ES EL PUNTO 0, 0)

    ## LÍMITE DE BORDES DE LA PANTALLA, EVITAR QUE EL OBJETO SALGA DE LOS LÍMITES DE LA PANTALLA
    if jugadorX <= 0:
        jugadorX = 0
    
    if jugadorX >= 736: ## 736 debido al tamaño de la pantalla(800) y al tamaño de la imagen (64) = 800 - 64 = 736
        jugadorX = 736

    
    ## MOVIMIENTO ENEMIGO
    for enemy in range(cantidadEnemigos):

        ## FIN DEL JUEGO
        if enemigoY[enemy] > 500:
            for enemyTemp in range(cantidadEnemigos):
                enemigoY[enemyTemp] = 1000  ## Se mueve a la posicion 1000, por lo tanto desaparece de la pantalla
            
            textoFinal()
            break

        enemigoX[enemy] += enemigoXCambio[enemy]

        if enemigoX[enemy] <= 0:
            enemigoXCambio[enemy] = 1    ## Cuanto toque un límite, el enemigo se moverá hacie el lado contrario
            enemigoY[enemy] += enemigoYCambio[enemy]
        if enemigoX[enemy] >= 736:
            enemigoXCambio[enemy] = -1
            enemigoY[enemy] += enemigoYCambio[enemy]

        colision = hayColision(enemigoX[enemy], enemigoY[enemy], balaX, balaY)
    
        if colision:
            sonidoColision = mixer.Sound(ruta + "\Golpe.mp3")
            sonidoColision.play()
            balay = 500
            balaVisible = False
            puntaje += 1
            enemigoX[enemy] = random.randint(0, 736)
            enemigoY[enemy] = random.randint(50, 200)

        enemigo(enemigoX[enemy], enemigoY[enemy], enemy)

    ## MOVIMIENTO BALA
    if balaY <= -64: ## Píxeles de alto de la vala, (Cuando la bala desparaece de la vista)
        balaY = 500
        balaVisible = False

    if balaVisible:
        dispararBala(balaX, balaY)
        balaY -= balaYCambio

    

    mostrarPuntaje(textoX, textoY)
    jugador(jugadorX, jugadorY)
    pygame.display.update()