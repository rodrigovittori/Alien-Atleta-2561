#pgzero

"""
# [M5.L4 - Actividad #2: "Funciones de movimiento"]
# Objetivo: Migrar la lógica de movimiento de los enemigos a una función avocada a ello

Pasos:
1º Crearemos las funciones actualizar_abeja() y actualizar_caja()



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

cartel_game_over = Actor("GO")

COOLDOWN_SALTO = 0.6 # tiempo de recarga habilidad salto (en segundos)
timer_salto = 0 # tiempo que debe pasar (en segundos) antes de que nuestro personaje pueda saltar nuevamente
anim = 1
nva_imagen = "alien" # "alien": quieto / "left": mov. izq. / "right" : mov. dcha. / "hurt": tomó daño
game_over = False
puntuacion = 0

"""  #####################
    # FUNCIONES PROPIAS #
   #####################  """

def animar(op):
    if op == 1:
        animate(personaje, tween="linear", duration=2, x = WIDTH-35, y = HEIGHT-45)
    elif (op == 2):
        animate(personaje, tween="bounce_start_end", duration=2, x = 35, y = 45)
    elif (op == 3):
        animate(personaje, tween="accel_decel", duration = 2, x= WIDTH - 35, y = HEIGHT-45)
    else:
        animate(personaje, tween="bounce_start_end", duration = 2, x= 35, y = HEIGHT-45)

def actualizar_abeja():
    global puntuacion

    # Vamos a chequear que la abeja esté dentro de la pantalla
    if (abeja.x < (-int(abeja.width))):
         # Si se salió de la pantalla, la reseteo y sumo un punto
        puntuacion += 1
        abeja.x = WIDTH + 150
        
    else:
        abeja.x -= 5

def actualizar_caja():
    global puntuacion
    # To-do: migrar a una función
        
    if (caja.x < (-int(caja.width))):
        # Si se salió de la pantalla, la reseteo y sumo un punto
        puntuacion += 1
        caja.x = WIDTH
        
    else:
        caja.x -= 5 # mover la caja 5 px a la izquierda en cada frame
        
    caja.angle += 5
    if caja.angle > 360:
        caja.angle -= 360
    
def mover_personaje():
    global nva_imagen, timer_salto
    nva_imagen = "alien"
        
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

    # SALTO
    
    if ((keyboard.space or keyboard.w or keyboard.up) and (timer_salto <= 0) and (personaje.y > int(personaje.height / 2))):
        timer_salto = COOLDOWN_SALTO
        personaje.y -= personaje.height
        animate(personaje, tween="bounce_end", duration = 2, y=240)

def detectar_colisiones():
    global nva_imagen, game_over
    if ((personaje.colliderect(caja)) or (personaje.colliderect(abeja))):
        if nva_imagen != "hurt":
            nva_imagen = "hurt"
        game_over = True

def reiniciar_juego():

    global game_over, nva_imagen, timer_salto, puntuacion
    
    game_over = False
    personaje.pos = (50, 240)
    nva_imagen = 'alien'
    timer_salto = 0
    caja.pos = (WIDTH + caja.width, 265)
    caja.angle = 0
    abeja.pos = (WIDTH + 350, 150)
    puntuacion = 0

"""  ####################
    # FUNCIONES PGZERO #
   ####################  """

def draw():
    if (game_over):
        fondo.draw()
        cartel_game_over.draw()
        screen.draw.text(("Enemigos esquivados: " + str(puntuacion)), center= (int(WIDTH/2), 2* int(HEIGHT/3)), color ="yellow", fontsize=24)
        screen.draw.text("Presiona [Enter] para reiniciar", center= (int(WIDTH/2), 4* int(HEIGHT/5)), color = "white", fontsize = 32)

    else:
        fondo.draw()
        personaje.draw()
        caja.draw()
        abeja.draw()

        screen.draw.text(("Puntuacion: " + str(puntuacion)), midleft=(15, 15), color ="white", fontsize=24)
        
        if (timer_salto <= 0):
            screen.draw.text("¡LISTO!", midright=(WIDTH - 20,20), color = (0, 255, 0), fontsize=24)
        else:
            screen.draw.text(str(timer_salto), midright=(WIDTH - 20,20), color = "red", fontsize=24)    

def update(dt): # Podemos traducir "update" como "actualizar", es decir, en ella contendremos el código que produzca cambios en nuestro juego

    global timer_salto, nva_imagen

    if game_over:
        # En caso de game_over
        if (keyboard.enter) or keyboard.space:
            reiniciar_juego()
    
    else:

        
        #######################
        # CAMBIOS AUTOMATICOS #
        #######################
        
        timer_salto -= dt
        personaje.timer_agachado -= dt
        
        if (personaje.timer_agachado <= 0) and (personaje.esta_agachado):
            personaje.y = 240
            personaje.esta_agachado = False

        # Actualizamos los enemigos
        # Nota: creo que ésto después lo migramos a otra función
        actualizar_caja()
        actualizar_abeja()

        mover_personaje()

        detectar_colisiones()
        
        ### POST INPUT ###
    
        personaje.image = nva_imagen # Actualizamos el sprite del personaje

"""def on_key_down(key):
    
    global anim

    if (keyboard.space):
        animar(anim)
        anim += 1
        
        if anim >= 5:
            anim = 1   """