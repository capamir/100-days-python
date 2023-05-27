from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        """initialize a food object in screen"""
        super().__init__()
        self.setup()
        self.make()

    def setup(self):
        """craete a circle blue object named as 'food' with a radius of 10"""
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
    
    def make(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
