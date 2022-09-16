#Integrantes
#Julia Pasten Da Silva A01660665
#Luis Roberto Martinez Rodriguez

#Instrucciones
#Contar y desplegar el numero de taps
#Detectar cuando todos los cuadros se han destapado
#Centrar el dígito en el cuadro
#Como un condimento de innovación al juego, Podrías utilizar algo diferente a los dígitos para resolver el juego y que al usuario le ayude a tener mejor memoria ?


from ctypes import sizeof
from itertools import count
from random import *
from turtle import *
from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
#creamos la variable parejas y numero de taps que usaremos luego
tapn = 0
parejas = 0


def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'pink')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()

def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200

def tap(x, y):
    "Update mark and hidden tiles based on tap."
    #se globaliza la variable numero de taps para que no se confunda y asi le determinamos que cuente el numero de taps cada que el usuario presione la tecla
    global tapn
    tapn  = tapn +1
    print(tapn)
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        #Globaizamos la variable parejas para que no se confunda con la condicional
        global parejas
        parejas = parejas + 1
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        #se crea una condicional donde se cuenta el numero de parejas hasta legar al 32 que es el total para asi imprimir en la terminal que el juego se acabo
    if(parejas == 32):
        print("GAME OVER")

def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        #pasar a string tiles en la posicion mark 
        obj = str(tiles[mark])
        #creamos una condicional donde se evalua si obj tiene 2 numeros para alinearlo respectivamente 
        if(len(obj)==2):
            write(obj,align = "left",font=('Arial', 40, 'normal'))
        #y si es un numero nada mas se le coloca el espacio para la alineación
        else:
            write(" "+obj,align = "left",font=('Arial', 40, 'normal'))
    update()
    ontimer(draw, 100)

shuffle(tiles)
#print(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
