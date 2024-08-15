#pgzero

# M5.L1 - Actividad #2: "Ventana del Juego"
# Objetivo: presentar el sistema de pgzero a los alumnos

WIDTH = 480 # Ancho de la pantalla (en px)
HEIGHT = 480 # Alto de la pantalla (en px)

TITLE = "TITULO ÉPICO" # sin archivos
FPS = 30 # Tope/Límite de FPS (cuadros por segundo) a dibujar

#fondo = Actor("fondo_desierto")
#cactus = Actor("cactus", (360, 400))
#personaje = Actor("alien", (50, 370))
#plankton = Actor("plankton", bottomleft=(250, 420))

def draw():
    screen.fill(("#dc7d83"))
    screen.draw.text(TITLE, center=(WIDTH/2, HEIGHT/2), color="white", background="black", fontsize = 48)
    #fondo.draw()
    #cactus.draw()
    #personaje.draw()