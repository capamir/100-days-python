from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from score_board import ScoreBoard

class Game:
    def __init__(self):
        """Initial the Snake game in a 600*600 screen"""
        self.screen = Screen()
        self._setup()
        self.game()
        self.screen.exitonclick()

    def _setup(self):
        """Screen basic setup such as size and title and classes that need to be defined"""
        # screen setup 
        self.screen.setup(width=600, height=600)
        self.screen.title('Snake Game')
        self.screen.bgcolor('black')
        self.screen.tracer(0)
        
        # classes
        self.scoreboard = ScoreBoard()
        self.snake = Snake()
        self.food = Food()

        # keyboard cotrols 
        self.keys()
        self.screen.update()

    def keys(self):
        """keyboard setup for moving the snake around"""
        self.screen.listen()
        # W S A D keys
        self.screen.onkey(key='w', fun=self.snake.turn_up)
        self.screen.onkey(key='s', fun=self.snake.turn_down)
        self.screen.onkey(key='d', fun=self.snake.turn_right)
        self.screen.onkey(key='a', fun=self.snake.turn_left)

        # arrow keys
        self.screen.onkey(key='Up', fun=self.snake.turn_up)
        self.screen.onkey(key='Down', fun=self.snake.turn_down)
        self.screen.onkey(key='Right', fun=self.snake.turn_right)
        self.screen.onkey(key='Left', fun=self.snake.turn_left)

    def move(self):
        """Move the snake by using move method from snake class"""
        self.snake.move()
        self.screen.update()
        sleep(0.15)

    def game_over(self):
        self.scoreboard.reset()
        self.snake.reset()

    def game(self):
        """Play the game using while loop"""
        self.game_is_on = True
        while self.game_is_on:
            self.move()
            # detect collision with the food
            if self.snake.head.distance(self.food) < 15:
                self.scoreboard.take_point
                self.food.make()
                self.snake.eat()

            # detect collision with the wall
            if self.snake.hit_wall():
                self.game_over()
            
            # detect collision with the tail
            for segment in self.snake.body[1:]:
                # if head colides with any segment in the tail
                if self.snake.head.distance(segment) < 10: 
                    # trigger game over
                    self.game_over()

Game()
