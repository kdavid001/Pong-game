from turtle import Turtle


class CompPaddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)
        self.setpos(-350, 0)

    def move_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def move_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)
