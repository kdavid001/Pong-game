from turtle import Turtle, Screen

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME!")

paddle = Turtle()
paddle.color('white')
paddle.penup()
paddle.shape("square")
paddle.shapesize(5, 1)
paddle.setpos(350, 0)


def up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def down():
    new_y2 = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y2)


screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")

screen.exitonclick()
