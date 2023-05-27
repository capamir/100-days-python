from turtle import Screen
from time import sleep
from snake import Snake


class Game:
    def __init__(self):
        self.screen = Screen()
        self.setup()
        self.keys()
        self.game()
        self.screen.exitonclick()

    def setup(self):
        self.screen.setup(width=600, height=600)
        self.screen.title('Snake Game')
        self.screen.bgcolor('black')
        self.screen.tracer(0)

        self.snake = Snake()
        self.screen.update()

    def keys(self):
        self.screen.listen()
        # W S A D keys
        self.screen.onkey(key='w', fun=self.snake.turn_up)
        self.screen.onkey(key='s', fun=self.snake.turn_down)
        self.screen.onkey(key='d', fun=self.snake.turn_right)
        self.screen.onkey(key='a', fun=self.snake.turn_left)
        self.screen.onkey(key='c', fun=self.snake.clear)
    
        # arrow keys
        self.screen.onkey(key='Up', fun=self.snake.turn_up)
        self.screen.onkey(key='Down', fun=self.snake.turn_down)
        self.screen.onkey(key='Right', fun=self.snake.turn_right)
        self.screen.onkey(key='Left', fun=self.snake.turn_left)

    def move(self):
        self.snake.move()
        self.screen.update()
        sleep(0.1)

    def game(self):
        game_is_on = True
        while game_is_on:
            self.move()

Game()
