from square import Square


class Snake:
    starting_positions = [ (0, 0), (-20, 0), (-40, 0) ]
    directions = {'right': 0, 'up': 90, 'left': 180, 'down': 270}
    
    def __init__(self):
        """initial the snake body in the center of the screen"""
        self.body = []
        self._create()
        self.head = self.body[0]
        self.tail = self.body[-1]

    def _create(self):
        """create a new Snake with the given starting positions"""
        for position in self.starting_positions:
            self.body.append( Square(position) )

    def eat(self):
        """eat the Food and increase a square to body of the snake """
        tail_pos = self.tail.position()
        self.body.append( Square(tail_pos) )


    def move(self):
        """move the snake from last square of snake's body in direction of the snake's head"""
        for seg_idx in range(len(self.body)-1, 0, -1):
            cor = self.body[seg_idx-1].position() # last sqaure cor
            self.body[seg_idx].goto(cor)
        self.head.move_forward()
    
    
    def turn_left(self):
        """Turns snake's head to leftside only if head is not heading right """
        if self.head.heading() != self.directions['right']:
            self.head.turn('left')


    def turn_right(self):
        """Turns snake's head to leftside only if head is not heading left """
        if self.head.heading() != self.directions['left']:
            self.head.turn('right')

        
    def turn_up(self):
        """Turns snake's head to leftside only if head is not heading down """
        if self.head.heading() != self.directions['down']:
            self.head.turn('up')


    def turn_down(self):
        """Turns snake's head to leftside only if head is not heading up """
        if self.head.heading() != self.directions['up']:
            self.head.turn('down')
    
    def hit_wall(self):
        if (self.head.xcor() > 280 or self.head.xcor() < -280) or \
            (self.head.ycor() > 280 or self.head.ycor() < -280):
            return True
    
    def clear(self):
        pass

