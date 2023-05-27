from turtle import Turtle, Screen

class Timmy:
    def __init__(self, shape='turtle', color=None):
        tim = Turtle()
        tim.shape(shape)
        if color:
            tim.color(color)
        self.tim = tim


    def turn_left(self):
        self.tim.left(10)


    def turn_right(self):
        self.tim.right(10)
        
    def up(self):
        self.tim.forward(10)

    def down(self):
        self.tim.backward(10)
    
    def clear(self):
        self.tim.clear()
        self.tim.pu()
        self.tim.home()
        self.tim.pd()


class ControlScreen:
    def __init__(self):
        self.timmy = Timmy()
        self.screen = Screen()
        self.screen.listen()

        self.moves()
        
        self.screen.exitonclick()
    
    def moves(self):
        self.screen.onkey(key='w', fun=self.timmy.up)
        self.screen.onkey(key='s', fun=self.timmy.down)
        self.screen.onkey(key='d', fun=self.timmy.turn_right)
        self.screen.onkey(key='a', fun=self.timmy.turn_left)
        self.screen.onkey(key='c', fun=self.timmy.clear)


ControlScreen()