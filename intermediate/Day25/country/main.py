from turtle import Screen, shape, Turtle
from pandas import read_csv, DataFrame

class Country:
    def __init__(self):
        self.screen = Screen()
        self._screen_setup()
        self.guessed_states = []
        self.data()
        self.game()
        self.screen.exitonclick()

    def _screen_setup(self):
        self.screen.title("U.S. State Game")
        image = "blank_states_img.gif"
        self.screen.addshape(image)
        
        shape(image)

    def data(self):
        self.data = read_csv("50_states.csv")
        self.states = self.data.state.to_list()
    
    def ask(self):
        return self.screen.textinput(title=f"{len(self.guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    def exit(self):
        missing_states = []
        for state in self.states:
            if state not in self.guessed_states:
                missing_states.append(state)
        new_data = DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")


    def game(self):
        while len(self.guessed_states) < 50:
            answer_state = self.ask()
            if answer_state == "Exit":
                self.exit()                
                break
        
            if answer_state in self.states:
                self.guessed_states.append(answer_state)
                t = Turtle()
                t.hideturtle()
                t.penup()
                state_data = self.data[self.data.state == answer_state]
                t.goto(int(state_data.x), int(state_data.y))
                t.write(answer_state)


Country()
