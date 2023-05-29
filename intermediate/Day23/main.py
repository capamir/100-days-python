import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


class Game:
    def __init__(self):
        self._screen_setup()
        # classes
        self.player = Player()
        self.car_manager = CarManager()
        self.board = Scoreboard()

        self._keys()
        self.game()
        self.screen.exitonclick()

    def _screen_setup(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.tracer(0)
        


    def _keys(self):
        """keyboard setup for moving the turtle around"""
        self.screen.listen()

        # Up and Down arrow keys => right paddle
        self.screen.onkey(key='Up', fun=self.player.move_up)
        self.screen.onkey(key='Down', fun=self.player.move_down)


    def car_collision(self):
        for car in self.car_manager.cars:
            if car.distance(self.player) < 20:
                self.game_is_on = False
                self.board.game_over()
    
    def turtle_crossing(self):
        if self.player.is_finished():
            self.level_up()


    def level_up(self):
        self.player.refresh()
        self.car_manager.level_up()
        self.board.level_up()

    def game(self):
        self.game_is_on = True
        while self.game_is_on:
            time.sleep(0.1)
            self.screen.update()

            self.car_manager.craete()
            self.car_manager.move_cars()

            # Detect collision with car
            self.car_collision()

            # Detect successful crossing
            self.turtle_crossing()
            
Game()