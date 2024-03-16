from turtle import Turtle


class Scores(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.penup()
        self.setposition(0, 250)
        self.color('white')
        self.hideturtle()
        self.pad_score = 0
        self.comp_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(arg=f"{self.pad_score}", align='center', font=('Arial', 30, 'normal'))
        self.goto(100, 200)
        self.write(arg=f"{self.comp_score}", align='center', font=('Arial', 30, 'normal'))

    def paddle_point(self):
        self.pad_score += 1
        self.update()

    def computer_point(self):
        self.comp_score += 1
        self.update()
