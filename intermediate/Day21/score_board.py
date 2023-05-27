from turtle import Turtle

class ScoreBoard(Turtle):
    font = ("Arial", 24, "normal")
    alignment = "center"

    def __init__(self):
        super().__init__()
        self.score = 0
        self.position = (0, 260)

        self.setup()
        self.show()

    def setup(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(self.position)

    def show(self):
        self.write(f"Score: {self.score}", align=self.alignment, font=self.font)

    def game_over(self):
        position = (0, 0)
        self.goto(position)
        self.write("Game over", align=self.alignment, font=self.font)

    @property
    def take_point(self):
        self.score += 1
        self.clear() # clear the previous text that was written
        self.show()