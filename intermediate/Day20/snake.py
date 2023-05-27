from square import Square


class Snake:
    starting_position = [ (0, 0), (-20, 0), (-40, 0) ]
    directions = {'right': 0, 'up': 90, 'left': 180, 'down': 270}
    
    def __init__(self):
        self.body = []
        self._create()
        self.head = self.body[0]

    def _create(self):
        for position in self.starting_position:
            self.body.append( Square(position) )

    def move(self):
        for seg_idx in range(len(self.body)-1, 0, -1):
            cor = self.body[seg_idx-1].cordinates() # last sqaure cor
            self.body[seg_idx].goto(cor)
        self.head.forward()
    
    
    def turn_left(self):
        if self.head.heading() != self.directions['right']:
            self.head.turn('left')


    def turn_right(self):
        if self.head.heading() != self.directions['left']:
            self.head.turn('right')

        
    def turn_up(self):
        if self.head.heading() != self.directions['down']:
            self.head.turn('up')


    def turn_down(self):
        if self.head.heading() != self.directions['up']:
            self.head.turn('down')
        
    
    def clear(self):
        self.tim.clear()
        self.tim.pu()
        self.tim.home()

