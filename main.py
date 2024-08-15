#pgzero

"""
# M5.L1 - Actividad #4: "Personaje"
# Objetivo: enseñar a los alumnos a crear Actores y mostrarlos por pantalla
"""
WIDTH = 600 # Ancho de la ventana (en px)
HEIGHT = 300 # Alto de la ventana (en px)

TITLE = "Juego del Alien Atleta y sus piruetas" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo

# Actores
fondo = Actor("background")
personaje = Actor("alien", (50, 240))

def draw():
    fondo.draw()
    personaje.draw()