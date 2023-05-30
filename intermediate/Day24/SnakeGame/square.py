from turtle import Turtle


class Square(Turtle):
    directions = {'right': 0, 'up': 90, 'left': 180, 'down': 270}

    def __init__(self, pos):
        """initial a white square in the given position"""
        super().__init__()
        self.shape('square')
        self.color("white")
        self.pu()
        self.goto(pos)
    

    def turn(self, dirc):
        """Turn the square direction to given direction"""
        direction = self.directions[dirc]
        self.setheading(direction)

    def move_forward(self, steps=20):
        """move the square forward by given steps if not default value of steps is 20"""
        self.forward(steps)
