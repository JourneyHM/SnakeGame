"""
Juego: Snake

Programador 1: Iván Santiago Hernández Mendoza - A01662556
Programador 2: Diego Jacobo Martínez - A01656583 

Fecha: 9 / 05 / 2022
"""

from random import randint, randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colours = ['black','green','yellow','purple','blue']    # Se añade una lista de colores
colour = randint(0,4)                                   # Se inicializan variables para escoger
colourF = randint(0,4)                                  # al azar el color de la serpiente y la comida
while (colour==colourF): colourF = randint(0,4)         # Se compara si son iguales los colores, si si lo son se cambian

def getColour(i):               # Se hace un metodo para obtener el color de la lista
    colour = colours[i]
    return colour


def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    head = snake[-1].copy()
    head.move(aim)


    foodMoves = randint(0,3)

    if (foodMoves == 0):                                 # Movimiento de la comida un paso a la vez
        foodAim = randint(0,3)
        if (foodAim == 0) & (inside(food)==True):
            food.move(vector(0, -10))
        elif (foodAim == 1) & (inside(food)==True):
            food.move(vector(0, 10))
        elif (foodAim == 2) & (inside(food)==True):
            food.move(vector(10, 0))
        elif (foodAim == 3) & (inside(food)==True):
            food.move(vector(-10, 0))
        else:
            if(food.x == -200):
                food.move(vector(10, 0))
            elif(food.x == 190):
                food.move(vector(-10, 0))
            elif(food.y == -200):
                food.move(vector(0, 10))
            elif(food.y == 190):
                food.move(vector(0, -10))


    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, getColour(colour)) # Se cambia el color estatico por el aleatorio

    square(food.x, food.y, 9, getColour(colourF)) # Se cambia el color estatico por el aleatorio
    update()
    ontimer(move, 100)


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