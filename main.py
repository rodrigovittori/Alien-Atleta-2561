#pgzero

"""
# M5.L2 - Actividad #1: "Actualizando la caja"
# Objetivo: lograr que los obstáculos reaparezcan tras abandonar la ventana

1º Agregar condicion (if)
"""
WIDTH = 600 # Ancho de la ventana (en px)
HEIGHT = 300 # Alto de la ventana (en px)

TITLE = "Juego del Alien Atleta y sus piruetas" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo

# Actores
fondo = Actor("background")
personaje = Actor("alien", (50, 240))
caja = Actor("box", (WIDTH - 50, 240))

def draw():
    fondo.draw()
    personaje.draw()
    caja.draw()

def update(dt): # Podemos traducir "update" como "actualizar", es decir, en ella contendremos el código que produzca cambios en nuestro juego

    if (personaje.x > (WIDTH - int(personaje.width/2)) ):
        personaje.x = 0
    else:
        personaje.x +=5 # mover el personaje 5 px a la derecha en cada frame
    
    if (caja.x < (int(caja.width/2))):
        caja.x = WIDTH
    else:
        caja.x -= 5 # mover la caja 5 px a la izquierda en cada frame
    
    if caja.angle > 360:
        caja.angle -= 360
    caja.angle += 5