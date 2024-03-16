from turtle import *
from paddle import Paddle
from computerpaddle import CompPaddle
from ball import Ball
from scoreboard import Scores

scoreboard = Scores()
ball = Ball()
screen = Screen()
paddle = Paddle()
computer = CompPaddle()

screen.tracer(0)
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("PONG GAME!")

screen.listen()
# for paddle
screen.onkey(paddle.move_up, "Up")
screen.onkey(paddle.move_down, "Down")

# for computer paddle
screen.onkey(computer.move_up, "w")
screen.onkey(computer.move_down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # detection with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -260:
        ball.bounce()

    # detection of ball with paddle
    if (ball.distance(paddle)) < 50 and ball.xcor() > 320:
        ball.bounce_paddle()

    # detection of ball with computer
    elif (ball.distance(computer)) < 50 and ball.xcor() < -320:
        ball.bounce_paddle()

        # detection with left(computer) wall
    if ball.xcor() > 370:
        ball.reset_ball()
        scoreboard.paddle_point()
        scoreboard.update()

        # detection with right(paddle) wall
    elif ball.xcor() < -370:
        ball.reset_ball()
        scoreboard.computer_point()
        scoreboard.update()

screen.exitonclick()
