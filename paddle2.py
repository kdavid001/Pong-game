import turtle


class Paddle:
    def __init__(self):
        self.paddle = turtle.Turtle()
        self.paddle.color('white')

    def move(self, param):
        self.paddle.forward(100)

    def move_down(self, param):
        self.paddle.forward(20)

    def backward(self, param):
        self.paddle.forward(20)