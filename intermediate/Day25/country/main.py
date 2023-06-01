from turtle import Screen, shape, Turtle
from pandas import read_csv, DataFrame

class CountryName(Turtle):
    def __init__(self, pos, text):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(pos)
        self.write(text)



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
        return self.screen.textinput(
            title=f"{len(self.guessed_states)}/50 States Correct", 
            prompt="What's another state's name?"
            ).title()

    def exit(self):
        missing_states = [state for state in self.states if state not in self.guessed_states]
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
                
                state_data = self.data[self.data.state == answer_state]
                pos = (int(state_data.x), int(state_data.y))
                CountryName(pos, answer_state)


Country()
