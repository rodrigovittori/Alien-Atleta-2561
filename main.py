#pgzero

"""
# M5.L3 - Actividad #3: "Controles"
# Objetivo: Nuestro código anterior ya resuelve el ejercicio, así que sólo desharemos los cambios de assets

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

    if (keyboard.right or keyboard.d) and (personaje.x < (WIDTH - int(personaje.width/2)) ):
        personaje.x += 5

    elif (keyboard.left or keyboard.a) and (personaje.x > (int(personaje.width/2))):
        personaje.x -= 5
    
    
    if (caja.x < (int(caja.width/2))):
        caja.x = WIDTH
    else:
        caja.x -= 5 # mover la caja 5 px a la izquierda en cada frame
    
    if caja.angle > 360:
        caja.angle -= 360
    caja.angle += 5