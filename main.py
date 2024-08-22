#pgzero

"""
# M5.L3 - Actividad #5: "Salto"
# Objetivo: Agregar la lógica necesaria para implementar un salto

Nota: Revertimos los cambios por assets // opcional: dejar o eliminar la función anim como referencia

1º Revertimos los cambios por assets
2º vamos a crear las variables necesarias para el sistema de salto: COOLDOWN_SALTO y timer_salto
3º Agregamos como variable global timer_salto en updtae y en on_key_down
4º Comentamos el código de anim en on_key_down
5º Agregamos la lógica de control de salto (en on_key_down)
6º Agregamos un indicador de salto en draw()
"""

WIDTH = 600 # Ancho de la ventana (en px)
HEIGHT = 300 # Alto de la ventana (en px)

TITLE = "Juego del Alien Atleta y sus piruetas" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo

# Actores
fondo = Actor("background")
personaje = Actor("alien", (50, 240))
caja = Actor("box", (WIDTH - 50, 260))

COOLDOWN_SALTO = 0.6 # tiempo de recarga habilidad salto (en segundos)
timer_salto = 0 # tiempo que debe pasar (en segundos) antes de que nuestro personaje pueda saltar nuevamente
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
    caja.draw()

    if (timer_salto <= 0):
        screen.draw.text("¡LISTO!", midleft=(20,20), color = (0, 255, 0), fontsize=24)
    else:
        screen.draw.text(str(timer_salto), midleft=(20,20), color = "red", fontsize=24)    

def update(dt): # Podemos traducir "update" como "actualizar", es decir, en ella contendremos el código que produzca cambios en nuestro juego

    global timer_salto

    #######################
    # CAMBIOS AUTOMATICOS #
    #######################
    
    timer_salto -= dt

    # To-do: migrar a una función
    
    if (caja.x < (int(caja.width/2))):
        caja.x = WIDTH
    else:
        caja.x -= 5 # mover la caja 5 px a la izquierda en cada frame
    
    if caja.angle > 360:
        caja.angle -= 360
    caja.angle += 5
    
    ################
    # LEER TECLADO #
    ################
    
    if (keyboard.right or keyboard.d) and (personaje.x < (WIDTH - int(personaje.width/2)) ):
        personaje.x += 5

    elif (keyboard.left or keyboard.a) and (personaje.x > (int(personaje.width/2))):
        personaje.x -= 5
    

def on_key_down(key):
    
    global anim, timer_salto

    if (keyboard.space or keyboard.w or keyboard.up) and (timer_salto <= 0) and (personaje.y > int(personaje.height / 2)):
        timer_salto = COOLDOWN_SALTO
        personaje.y -= personaje.height
        animate(personaje, tween="bounce_end", duration = 2, y=240)
    
    """if (keyboard.space):
        animar(anim)
        anim += 1
        
        if anim >= 5:
            anim = 1   """