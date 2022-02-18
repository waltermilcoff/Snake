from operator import index
import turtle
import time
import random

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("cadetblue")
s.title("Snake by Walter Milcoff")


comida = turtle.Turtle()


comida.shape("circle")
comida.color("orange")
comida.penup()
comida.goto(0, 100)
comida.speed(0)


snake = turtle.Turtle()


snake.speed(1)
snake.shape("arrow")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"
snake.color("red")


cuerposnake = []


retraso = 0.1


def arriba():
    snake.direction = "up"
    
def abajo():
    snake.direction = "down"
    
def derecha():
    snake.direction = "right"
    
def izquierda():
    snake.direction = "left"
    
    
def movimiento():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)


s.listen()

s.onkeypress(arriba, "Up")
s.onkeypress(abajo, "Down")
s.onkeypress(derecha, "Right")
s.onkeypress(izquierda, "Left")


while True:
    s.update()
    
    if snake.xcor() > 300 or snake.xcor() < -300 or snake.ycor() > 300 or snake.ycor() < -300:
        time.sleep(3)
        for i in cuerposnake:
            i.clear()
            i.hideturtle()
        snake.home()
        snake.direction = "stop"
        cuerposnake.clear()    
        

    if snake.distance(comida) < 20:
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        comida.goto(x,y)
        
        nuevo_cuerpo = turtle.Turtle()
        nuevo_cuerpo.shape("arrow")
        nuevo_cuerpo.color("red")
        nuevo_cuerpo.penup()
        nuevo_cuerpo.goto(0,0)
        nuevo_cuerpo.speed(0)
        cuerposnake.append(nuevo_cuerpo)
        
    total = len(cuerposnake)
        
    for index in range(total -1, 0, -1):
        x = cuerposnake[index-1].xcor()
        y = cuerposnake[index-1].ycor()
        cuerposnake[index].goto(x,y)
            
    if total > 0:
        x = snake.xcor()
        y = snake.ycor()
        cuerposnake[0].goto(x,y)
        
    movimiento()
    
    for i in cuerposnake:
        if i.distance(snake) < 20:
            for i in cuerposnake:
                i.clear()
                i.hideturtle()
            snake.home()
            cuerposnake.clear()
            snake.direction = "stop"

         
    time.sleep(retraso)

turtle.done()

