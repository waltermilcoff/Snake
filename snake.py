import turtle
import time

s = turtle.Screen()
s.setup(650,650)
s.bgcolor("cadetblue")
s.title("Snake by Walter")

snake = turtle.Turtle()

snake.speed(1)
snake.shape("arrow")
snake.penup()
snake.goto(0,0)
snake.direction = "stop"
snake.color("red")

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
    movimiento()
    time.sleep(retraso)


turtle.done()

