#pgzero

"""
# [M5.L3 - Actividad #2: "Colisión con una abeja"]
# Objetivo: Agregar lógica de colisión para la abeja

NOTA: En el programa han eliminado la actividad donde creábamos la abeja, así que toca crearla en éste ejercicio.

1º Crear actor abeja
2º La agregamos en nuestro draw()
3º Agregamos los controles de movimiento automático para la abeja
4º Agregamos la condición de colliderect() con un "or"

"""

WIDTH = 600 # Ancho de la ventana (en px)
HEIGHT = 300 # Alto de la ventana (en px)

TITLE = "Juego del Alien Atleta y sus piruetas" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo

# Actores
fondo = Actor("background")
personaje = Actor("alien", (50, 240))
personaje.timer_agachado = 0.0 # Tiempo restante (en segundos) antes de poner de pie al personaje
personaje.esta_agachado = False
caja = Actor("box", (WIDTH - 50, 260))
abeja = Actor("bee", (WIDTH + 150, 150))

COOLDOWN_SALTO = 0.6 # tiempo de recarga habilidad salto (en segundos)
timer_salto = 0 # tiempo que debe pasar (en segundos) antes de que nuestro personaje pueda saltar nuevamente
anim = 1
nva_imagen = "alien" # "alien": quieto / "left": mov. izq. / "right" : mov. dcha. / "hurt": tomó daño

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
    abreja.draw()

    if (timer_salto <= 0):
        screen.draw.text("¡LISTO!", midleft=(20,20), color = (0, 255, 0), fontsize=24)
    else:
        screen.draw.text(str(timer_salto), midleft=(20,20), color = "red", fontsize=24)    

def update(dt): # Podemos traducir "update" como "actualizar", es decir, en ella contendremos el código que produzca cambios en nuestro juego

    global timer_salto, nva_imagen

    #######################
    # CAMBIOS AUTOMATICOS #
    #######################
    
    timer_salto -= dt
    personaje.timer_agachado -= dt
    
    nva_imagen = "alien" # Si el personaje NO se mueve, mostraremos esta imágen
    
    if (personaje.timer_agachado <= 0) and (personaje.esta_agachado):
        personaje.y = 240
        personaje.esta_agachado = False

    # To-do: migrar a una función
    
    if (caja.x < (int(caja.width/2))):
        caja.x = WIDTH
    else:
        caja.x -= 5 # mover la caja 5 px a la izquierda en cada frame
    
    if caja.angle > 360:
        caja.angle -= 360
    caja.angle += 5

    # Vamos a chequear que la abeja esté dentro de la pantalla
    
    if (abeja.x < -30):
        abeja.x = WIDTH + 150
    else:
        abeja.x -= 5
    
    ################
    # LEER TECLADO #
    ################
    
    if (keyboard.right or keyboard.d) and (personaje.x < (WIDTH - int(personaje.width/2)) ):
        personaje.x += 5
        nva_imagen = "right"

    elif (keyboard.left or keyboard.a) and (personaje.x > (int(personaje.width/2))):
        personaje.x -= 5
        nva_imagen = "left"
    
    elif (keyboard.down or keyboard.s):
        personaje.y = 260
        nva_imagen = "duck"
        personaje.timer_agachado = 0.1
        personaje.esta_agachado = True

    ##############
    # COLISIONES #
    ##############

    # To - do: migrar a función
  
    if (personaje.colliderect(caja) or personaje.colliderect(abeja)):
      if nva_imagen != "hurt":
        nva_imagen = "hurt"
    
    ### POST INPUT ###

    personaje.image = nva_imagen # Actualizamos el sprite del personaje

def on_key_down(key):
    
    global anim, timer_salto

    if ((keyboard.space or keyboard.w or keyboard.up) and (timer_salto <= 0) and (personaje.y > int(personaje.height / 2))):
        timer_salto = COOLDOWN_SALTO
        personaje.y -= personaje.height
        animate(personaje, tween="bounce_end", duration = 2, y=240)
    
    """if (keyboard.space):
        animar(anim)
        anim += 1
        
        if anim >= 5:
            anim = 1   """