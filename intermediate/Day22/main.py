from turtle import Screen
from paddles import RightPadle, LeftPadle
from ball import Ball
from board import ScoreBoard
import time

class Game:
    def __init__(self):
        self.screen = Screen()
        self._setup()
        self.game()

        self.screen.exitonclick()

    def _setup(self):
        """Screen basic setup such as size and title and classes that need to be defined"""
        # screen setup 
        self.screen.setup(width=800, height=600)
        self.screen.title('Snake Game')
        self.screen.bgcolor('black')
        self.screen.tracer(0)

        # classes that need to be defined
        self.right_paddle = RightPadle()
        self.left_paddle = LeftPadle()
        self.ball = Ball()
        self.board = ScoreBoard()
        self.screen.update()

        # keyboard controls
        self._keys()

    def _keys(self):
        """keyboard setup for moving the paddles around"""
        self.screen.listen()
        # W S keys => left padde
        self.screen.onkey(key='w', fun=self.left_paddle.turn_up)
        self.screen.onkey(key='s', fun=self.left_paddle.turn_down)

        # Up and Down arrow keys => right paddle
        self.screen.onkey(key='Up', fun=self.right_paddle.turn_up)
        self.screen.onkey(key='Down', fun=self.right_paddle.turn_down)

    def move(self):
        self.ball.move()
        self.screen.update()
        time.sleep(self.ball.move_speed)

    def game(self):
        game_is_on = True
        while game_is_on:
            self.move()

            # Detect collision with wall
            if self.ball.ycor() > 280 or self.ball.ycor() < -280:
                # ball hit wall and needs to bounce
                self.ball.bounce_y()
            
            
            # Detect that the ball goes out of bounds edge 
            if self.ball.xcor() > 320 or self.ball.xcor() < -320:
                # Detect collision with paddles
                if self.ball.distance(self.right_paddle) < 45 or \
                    self.ball.distance(self.left_paddle) < 45:
                    self.ball.bounce_x()

                # right paddle missed the ball
                elif self.ball.xcor() > 380:
                    self.ball.refresh()
                    self.board.left_take_point()

                # left paddle missed the ball
                elif self.ball.xcor() < -380:
                    self.ball.refresh()
                    self.board.right_take_point()

Game()
