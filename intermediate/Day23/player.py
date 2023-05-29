from turtle import Turtle


class Player(Turtle):
    STARTING_POSITION = (0, -280)
    MOVE_DISTANCE = 10
    FINISH_LINE_Y = 280

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.refresh()

    def move_up(self):
        self.forward(self.MOVE_DISTANCE)

    def move_down(self):
        self.backward(self.MOVE_DISTANCE)

    def is_finished(self):
        return self.ycor() > self.FINISH_LINE_Y
    
    def refresh(self):
        self.goto(self.STARTING_POSITION)
