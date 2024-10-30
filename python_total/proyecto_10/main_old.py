import pygame
import random
import math

pygame.init()

puntuacion = 0

# Crear la pantalla
pantalla = pygame.display.set_mode((800, 600))

# Configurar la pantalla
pygame.display.set_caption('Invasión Espacial')
icono = pygame.image.load('ovni.png')
pygame.display.set_icon(icono)
fondo = pygame.image.load('fondo.jpg')

# Configurar jugador
img_jugador = pygame.image.load('cohete.png')
jugador_eje_x = 800 / 2 - 64 / 2  # Le quito la mitad de su tamaño 64 x 64
jugador_eje_y = 600 - 64  # Para que toque el piso le quito la altura de la nave
jugador_eje_x_gap = 0

# Configurar enemigo
img_enemigo = []
enemigo_eje_x = []
enemigo_eje_y = []
enemigo_eje_x_gap = []
enemigo_eje_y_gap = []
enemigo_vivo = []

cantidad_enemigos = 8
for i in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load('enemigo.png'))
    enemigo_eje_x.append(random.randint(1, 800 - 64))  # Le quito su tamaño 64 x 64
    enemigo_eje_y.append(random.randint(1, 200))
    enemigo_eje_x_gap.append(0.1)
    enemigo_eje_y_gap.append(25)
    enemigo_vivo.append(True)

# Configurar bala
img_bala = pygame.image.load('bala.png')
bala_eje_x = 0
bala_eje_y = 500
bala_eje_y_gap = 0.6
bala_visible = False

# Ubicar al jugador en la pantalla
def jugador(x, y):
    pantalla.blit(img_jugador, (x, y))

# Ubicar al jugador en la pantalla
def enemigo(img, x, y):
    pantalla.blit(img, (x, y))

# Ubicar al jugador en la pantalla
def bala(x, y):
    pantalla.blit(img_bala, (x, y))

def hay_colision(x_enemigo, y_enemigo, x_bala, y_bala):
    distancia = math.sqrt(math.pow(x_enemigo - x_bala, 2) + math.pow(y_enemigo - y_bala, 2))
    if distancia < 27:
        return True
    else:
        return False

# Gestionar los eventos hasta el quit
final = False
while not final:

    # pantalla.fill((205, 144, 228))
    pantalla.blit(fondo, (0, 0))

    for evento in pygame.event.get():
        # Evento Cerrar y Acabar
        if evento.type == pygame.QUIT:
            final = True

        # Evento presionar flechas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_eje_x_gap = -0.3
            elif evento.key == pygame.K_RIGHT:
                jugador_eje_x_gap = 0.3
            elif evento.key == pygame.K_SPACE:
                if not bala_visible:
                    bala_visible = True
                    bala_eje_x = jugador_eje_x + 64 / 2 - 32 / 2
                    bala_eje_y = jugador_eje_y - 32

        # Evento Soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_eje_x_gap = 0


    # Ubicación del jugador
    jugador_eje_x += jugador_eje_x_gap
    # Limito el movimiento lateral del jugador hasta los bordes
    if jugador_eje_x < 0:
        jugador_eje_x = 0
    elif jugador_eje_x > 800 - 64:
        jugador_eje_x = 800 - 64

    # Ubicación del enemigo
    for i in range(cantidad_enemigos):
        enemigo_eje_x[i] += enemigo_eje_x_gap[i]
        # Limito el movimiento lateral del enemigo hasta los bordes y cambio dirección y altura
        if enemigo_eje_x[i] < 0:
            enemigo_eje_x[i] = 0
            enemigo_eje_y[i] += enemigo_eje_y_gap[i]
            enemigo_eje_x_gap[i] = 0.1
        elif enemigo_eje_x[i] > 800 - 64:
            enemigo_eje_x[i] = 800 - 64
            enemigo_eje_y[i] += enemigo_eje_y_gap[i]
            enemigo_eje_x_gap[i] = -0.1

    # Ubicación de la bala
    if bala_visible:
        bala_eje_y -= bala_eje_y_gap
        if bala_eje_y < 0:  # Limitar hasta el borde superior de la pantalla
            bala_visible = False
        for i in range(cantidad_enemigos):
            if enemigo_vivo[i]:
                if hay_colision(enemigo_eje_x[i], enemigo_eje_y[i], bala_eje_x, bala_eje_y):
                    bala_visible = False
                    enemigo_vivo[i] = False
                    puntuacion += 1

    jugador(jugador_eje_x, jugador_eje_y)  # después del relleno o fondo de la pantalla para que no se borre
    for i in range(cantidad_enemigos):
        if enemigo_vivo[i]:
            enemigo(img_enemigo[i], enemigo_eje_x[i], enemigo_eje_y[i])
    if bala_visible:
        bala(bala_eje_x, bala_eje_y)

    pygame.display.update()

