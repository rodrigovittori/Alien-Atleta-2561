#pgzero

"""
# M5.L3 - Actividad #7: "Cambiando sprites"
# Objetivo: Agregar la lógica necesaria para que el sprite del personaje cambie según las acciones del jugador

Nota: La tarea 6 se cumple con el código de la actividad #5

1º: Crear variable para almacenar la imágen que vamos a asignar al actor en cada frame.
2º: Agregamos  en update como variable global la variable nva_imagen
3º: Asignamos un sprite por defecto al iniciar update (en la vble nva_imageb)
4º: Post-input actualizamos el sprite del personaje para que sea la imágen almacenada en nuestra variable

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
nva_imagen = "alien" # "alien": quieto / "left": mov. izq. / "right" : mov. dcha.

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

    global timer_salto, nva_imagen

    #######################
    # CAMBIOS AUTOMATICOS #
    #######################
    
    timer_salto -= dt
    nva_imagen = "alien" # Si el personaje NO se mueve, mostraremos esta imágen

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
        nva_imagen = "right"

    elif (keyboard.left or keyboard.a) and (personaje.x > (int(personaje.width/2))):
        personaje.x -= 5
        nva_imagen = "left"

    ### POST INPUT ###

    personaje.image = nva_imagen # Actualizamos el sprite del personaje

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