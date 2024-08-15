#pgzero

"""
# M5.L1 - Actividad #3: "La función draw()"
# Objetivo: presentar el sistema de pgzero a los alumnos

Event hooks en pgzero (funciones especiales):
https://pygame-zero.readthedocs.io/en/stable/hooks.html?highlight=hooks

Hacer transparente un png: https://onlinepngtools.com/create-transparent-png
Modificar tamaño de un png: https://onlinepngtools.com/resize-png

Actividad libre: Modificar éste código para mostrar un mensaje personalizado
                 por pantalla con Pgzero
"""

WIDTH = 480 # Ancho de la pantalla (en px)
HEIGHT = 480 # Alto de la pantalla (en px)

TITLE = "TITULO ÉPICO" # sin archivos
FPS = 30 # Tope/Límite de FPS (cuadros por segundo) a dibujar


def draw():
    screen.fill((220, 125, 131))
    screen.draw.text(TITLE, center=(WIDTH/2, HEIGHT/2), color="white", background="black", fontsize = 48)