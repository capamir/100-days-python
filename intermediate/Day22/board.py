from turtle import Turtle


class ScoreBoard(Turtle):
    position = {'left': (-100, 200), 'right': (100, 200)}
    font = ("Arial", 80, "normal")
    alignment = "center"

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0

        self._setup()
        self._show()
        
    def _setup(self):
        self.color("white")
        self.hideturtle()
        self.penup()
    
    def _show(self):
        self.goto(self.position["right"])
        self.write(self.right_score, align=self.alignment, font=self.font)
        
        self.goto(self.position["left"])
        self.write(self.left_score, align=self.alignment, font=self.font)

    def left_take_point(self):
        self.left_score += 1
        self.clear() # clear the previous text that was written
        self._show()
    
    def right_take_point(self):
        self.right_score += 1
        self.clear() # clear the previous text that was written
        self._show()