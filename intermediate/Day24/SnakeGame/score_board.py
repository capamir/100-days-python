from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.get_high_score()

        self.score = 0
        self.position = (0, 260)

        self._setup()
        self.show()

    def _setup(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(self.position)

    def show(self):
        self.clear() # clear the previous text that was written
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_high_score()
        self.score = 0
        self.show()

    def set_high_score(self):
        with open("data.txt", 'w') as f:
            f.write(str(self.score))
    
    def get_high_score(self):
        with open("data.txt") as f:
            score = f.read()
            self.high_score = int(score)


    @property
    def take_point(self):
        self.score += 1
        if self.score > self.high_score:
            self.set_high_score()
            self.get_high_score()
        self.show()