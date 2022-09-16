#Integrantes
#Julia Pasten Da Silva A01660665
#Luis Roberto Martinez Rodriguez

#Instrucciones:
#Uno de los dos añadirá las siguientes funcionalidades
#Un color nuevo
#Dibujar un círculo
#El otro compañero añadirá:
#Completar el rectángulo
#Completar el triángulo

from turtle import *
from freegames import vector
from math import *

def line(start, end):
    "Draw line from start to end."
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)
     
#Se estableceran los parametros e indicaciones que las lineas tienen que realizar para que la figura que se requiera por el usuario se pueda formar y rellenarla con el color que se requiera.

def square(start, end):
    "Draw square from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()


def circle(start,end,extent=360,steps=360):
    
    if extent<360 and steps==360:
        steps=extent
    
    radius = start.x - end.y
    theta=extent/steps
    step_size=2*radius*sin(radians(theta/2))
    begin_fill()
    left(theta/2)
    forward(step_size)
    for i in range(1,steps):
        left(theta)
        forward(step_size)
    
    left(theta/2)
    end_fill()




def rectangle(start, end):
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    forward(2*(end.x - start.x))
    left(90)
    forward(end.x - start.x)
    left(90)
    forward(2*(end.x - start.x))
    left(90)
    forward(end.x - start.x)
    left(90)

    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x,start.y)
    down()
    begin_fill()

    forward(start.x - start.y)
    left(60)
    forward(start.y - start.x)
    left(60)
    forward(start.x - start.y)
    left(60)
    end_fill()

    
    

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('yellow'), 'K')
onkey(lambda: color('black'), 'W')
onkey(lambda: color('pink'), 'G')
onkey(lambda: color('green'), 'B')
onkey(lambda: color('blue'), 'R')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
