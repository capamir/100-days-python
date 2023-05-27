from turtle import Turtle, Screen


class Race:
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
    start_pos = [ (-230, -100), (-230, -60), (-230, -20), (-230, 20), (-230, 60), (-230, 100) ]
    
    def __init__(self):
        self.is_race_on = False
        self.turtles = []

    def make_turtle(self):
        for i in range(6):
            turtle_obj = Turtle(shape='turtle')
            turtle_obj.color(self.colors[i])
            turtle_obj.penup()

            x_pos = self.start_pos[i][0]
            y_pos = self.start_pos[i][1]

            turtle_obj.goto(x=x_pos, y=y_pos)
            self.turtles.append(turtle_obj)


class ControlScreen:    
    def __init__(self):
        
        self.setup()
        user_bet = self.screen.textinput(
            title='make your bet', prompt="Whitch turtle will win the race? pick a color: ",
        )
        race = Race()
        race.make_turtle()

        self.screen.exitonclick()

    def setup(self):
        self.screen = Screen()
        self.screen.setup(width=500, height=400)
        # self.screen.listen()

    
ControlScreen()
