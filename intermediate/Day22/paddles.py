from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.color('white')
        self.setheading(90)
    
    def turn_up(self):
        self.forward(20)

    def turn_down(self):
        self.backward(20)


class RightPadle(Paddle):
    starting_position = (350, 0)

    def __init__(self):
        super().__init__()
        self.goto(self.starting_position)


class LeftPadle(Paddle):
    starting_position = (-350, 0)

    def __init__(self):
        super().__init__()
        self.goto(self.starting_position)
