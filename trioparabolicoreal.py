#Integrantes
#Julia Pasten Da Silva A01660665
#Luis Roberto Martinez Rodriguez

#Instrucciones:
#La velocidad del movimiento para el proyectil y los balones sea más rápida
#Hacer que el juego nunca termine, de manera que los balones al salir de la ventana se re posicionen.

from random import randrange
from turtle import *
from freegames import vector

ball = vector(-200, -200)
speed = vector(0.5, 0.5)
targets = []

def tap(x, y):
    "Respond to screen tap."
    if not inside(ball):
        ball.x = -199
        ball.y = -199
        speed.x = (x + 500) / 25 #Se aumenta la velocidad del proyectil
        speed.y = (y + 500) / 25 #Se aumenta la velocidad del proyectil

def inside(xy):
    "Return True if xy within screen."
    return -200 < xy.x < 200 and -200 < xy.y < 200

def draw():
    "Draw ball and targets."
    clear()

    for target in targets:
        goto(target.x, target.y)
        dot(20, 'blue')

    if inside(ball):
        goto(ball.x, ball.y)
        dot(10, 'purple')#Aumentamos el tamaño del proyectil y se cambio el color del proyectil

    update()

def move():
    "Move ball and targets."
    if randrange(40) == 0:
        y = randrange(-150, 150)
        target = vector(200, y)
        targets.append(target)

    for target in targets:
        target.x -= 0.5

    if inside(ball):
        speed.y -= 0.35
        ball.move(speed)

    dupe = targets.copy()
    targets.clear()

    for target in dupe:
        if abs(target - ball) > 13:
            targets.append(target)

    draw()

    for target in targets:
        if not inside(target):
            return

    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)
onscreenclick(tap)
move()
done()
