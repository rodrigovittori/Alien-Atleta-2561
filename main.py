#pgzero

"""
# M5.L2 - Actividad #2: "Claves"
# Objetivo: controlar a nuestro personaje mediante el teclado

# NOTA: Modificamos actores por cambio de assets en la tarea
1º Modificamos fondo de "background" a "bg"
2º Comentamos la declaración del Actor "caja"
3º Comentamos la llamada al método draw de la caja (en la fn draw)
4º Comentamos el código que controla (en la fn update) la caja

"""
WIDTH = 600 # Ancho de la ventana (en px)
HEIGHT = 300 # Alto de la ventana (en px)

TITLE = "Juego del Alien Atleta y sus piruetas" # Título para la ventana del juego
FPS = 30 # Número de fotogramas por segundo

# Actores
fondo = Actor("bg")
personaje = Actor("alien", (50, 240))
#caja = Actor("box", (WIDTH - 50, 240))

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