from tracemalloc import stop
import turtle

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


turtle.done()

