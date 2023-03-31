import turtle
import random

__Pen = turtle.Pen()


turtle.bgcolor("#333333")
__Pen.pencolor("#a490ff")
__Pen.penup()
__Pen.hideturtle()
__Pen.goto((-380), 0)
__Pen.write('Adivina el número entre 1 y 100', font = ('Monda', 36, 'bold'))
secret_number = random.randint(1, 100)
intentos = 0
while True:
    intento = turtle.numinput('Adivina el número','Ingresa un valor: ')
    intentos += 1
    __Pen.clear()
    if (intento == secret_number) :
        __Pen.goto((-200), 0)
        __Pen.write('Adivinaste!', font = ('Monda', 64, 'bold'))
        __Pen.goto((-200), (-100))
        __Pen.write(('Intentos: ' + str(intentos)), font = ('Monda', 64, 'bold'))
        break
    elif (intento < secret_number) :
        __Pen.goto((-250), (-50))
        __Pen.write('El número es muy bajo', font = ('Monda', 36, 'bold'))
    else :
        __Pen.goto((-250), (-50))
        __Pen.write('El número es muy alto', font = ('Monda', 36, 'bold'))
turtle.exitonclick()