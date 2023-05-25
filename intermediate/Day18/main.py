from turtle import Turtle, Screen, colormode
from random import randint, choice

class Timmy:
    directions = (0, 90, 180, 270)

    def __init__(self, shape="turtle", color=None):
        self.tim = Turtle()
        self.tim.shape(shape)
        if color:
            self.tim.color(color)  
        self.tim.speed('fastest')


    def square(self):
        for _ in range(4):
            self.dashed_line(5)
            self.tim.left(90)

    def dashed_line(self, num_range):
        for _ in range(num_range):
            self.tim.forward(10)
            self.tim.pu() # pen up
            self.tim.forward(10)
            self.tim.pd() # pen down

    def shapes(self):
        for i in range(3, 10):
            direction = 360 // i
            for j in range(i):
                self.tim.forward(100)
                self.tim.right(direction)

    def random_color(self):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return (r, g, b)
    
    def wall(self):
        self.tim.color(self.random_color())
        self.tim.setheading(choice(self.directions))
        self.tim.forward(20)

    def draw_wall(self):
        self.tim.pensize(15)
        self.tim.color(self.random_color())
        self.tim.setheading(choice(self.directions))
        self.tim.forward(20)

        for _ in range(100):
            self.wall()

    def circle(self):
        for i in range(0, 360, 5):
            self.tim.setheading(i)
            self.tim.color(self.random_color())
            
            self.tim.circle(100)


timmy = Timmy()
screen = Screen()
colormode(255)

timmy.circle()

screen.exitonclick()
