from turtle import *
from paddle2 import Paddle

screen = Screen()
paddle = Paddle()

screen.setup(1000, 800)
screen.bgcolor("black")
screen.title("PONG GAME!")


def backward():
    paddle.backward(20)


screen.listen()
screen.onkey(key="up", fun=paddle.move_up())
# screen.onkey( key="down", fun=paddle.move_down())
screen.onkey(key='s', fun=backward)

screen.exitonclick()
