from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self._setup()
        self.show_level()

    def _setup(self):
        self.hideturtle()
        self.penup()
    
    def game_over(self):
        self.goto(0, 0)
        self.write("Game over", align="center", font=FONT)
        
    def level_up(self):
        self.level += 1
        self.show_level()
    
    def show_level(self):
        self.clear()
        self.goto(-230, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)
