#Integrantes
#Julia Pasten Da Silva A01660665
#Luis Roberto Martinez Rodriguez
#La comida podrá moverse al azar un paso a la vez y no deberá de salirse de la ventana
#Cada vez que se corra el juego, la víbora y la comida deberán tener colores diferentes entre sí, pero al azar, de una serie de 5 diferentes colores, excepto el rojo.
from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -210 < head.x < 200 and -210 < head.y < 200 #Se cambio el rango para que el codigo fuera diferente

def move():
    colors=["yellow","blue","green","pink","purple"]#Se asigna un arreglo de colores

    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, "red") #Se le deja rojo ya que seria el error por esa razon no colocamos rojo en el arreglo de colores
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-17, 17) * 10
        food.y = randrange(-17, 17) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 10, colors[randrange(0,5)])#Manda a llamar de forma random los colores del arreglo

    square(food.x, food.y, 10, colors[randrange(0,5)])#Manda a llamar de forma random los colores del arreglo
    update()
    ontimer(move, 150)#aumento 30

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
