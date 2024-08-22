#pgzero

"""
# M5.L3 - Actividad #4: "Función animate()"
# Objetivo: Demostrar los distintos tipos de animación

Nota: Nuevamente hay cambio de assets - NO compartir código y sólo explicar y exponer

Cambios:
1º Actor fondo imagen de "background" a "bg"
2º Desactivar caja: (creación, draw y update)
----
3º Agregar varible que controla la animación
4º Agregar función de animaciones
5º Presentar función on_key_down()
"""

WIDTH = 600 # Ancho de la ventana (en px)
HEIGHT = 300 # Alto de la ventana (en px)

TITLE = "Juego del Alien Atleta y sus piruetas" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo

# Actores
fondo = Actor("bg")
personaje = Actor("alien", (50, 240))
#caja = Actor("box", (WIDTH - 50, 240))

anim = 1

def animar(op):
    if op == 1:
        animate(personaje, tween="linear", duration=2, x = WIDTH-35, y = HEIGHT-45)
    elif (op == 2):
        animate(personaje, tween="bounce_start_end", duration=2, x = 35, y = 45)
    elif (op == 3):
        animate(personaje, tween="accel_decel", duration = 2, x= WIDTH - 35, y = HEIGHT-45)
    else:
        animate(personaje, tween="bounce_start_end", duration = 2, x= 35, y = HEIGHT-45)

def draw():
    fondo.draw()
    personaje.draw()
    #caja.draw()

def update(dt): # Podemos traducir "update" como "actualizar", es decir, en ella contendremos el código que produzca cambios en nuestro juego

    if (keyboard.right or keyboard.d) and (personaje.x < (WIDTH - int(personaje.width/2)) ):
        personaje.x += 5

    elif (keyboard.left or keyboard.a) and (personaje.x > (int(personaje.width/2))):
        personaje.x -= 5
    
    """
    if (caja.x < (int(caja.width/2))):
        caja.x = WIDTH
    else:
        caja.x -= 5 # mover la caja 5 px a la izquierda en cada frame
    
    if caja.angle > 360:
        caja.angle -= 360
    caja.angle += 5
    """

def on_key_down(key):
    
    global anim
    
    if (keyboard.space):
        animar(anim)
        anim += 1
        
        if anim >= 5:
            anim = 1