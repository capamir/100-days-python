from turtle import Turtle


class Square:
    directions = {'right': 0, 'up': 90, 'left': 180, 'down': 270}

    def __init__(self, pos):
        self.square = Turtle("square")
        self.square.color("white")
        self.square.pu()
        self.square.goto(pos)
    
    def forward(self, steps=20):
        self.square.forward(steps)

    def goto(self, pos):
        self.square.goto(pos)

    def cordinates(self):
        x_cor = self.square.xcor()
        y_cor = self.square.ycor()
        return (x_cor, y_cor)
    
    def turn(self, dirc):
        direction = self.directions[dirc]
        self.square.setheading(direction)

    def heading(self):
        return self.square.heading()