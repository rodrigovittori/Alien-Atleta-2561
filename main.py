#pgzero

"""
# M5.L1 - Actividad #5: "La función update(dt)"
# Objetivo: familiarizarnos con la función update()
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

def update(dt):
    personaje.x += 5 # mover el personaje 5 px a la derecha en cada frame
    caja.x -= 5 # mover la caja 5 px a la izquierda en cada frame
    
    personaje.angle -= 5
    caja.angle += 5