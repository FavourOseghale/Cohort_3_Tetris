"""The Block class represents a Tetris block with an ID, rotation states, cell positions, and methods for moving,
rotating, and drawing the block on a Pygame screen."""


from graphics import *
import random

class Block(Rectangle):
    ''' Block class:
        Implement a block for a tetris piece
        Attributes: x - type: int
                    y - type: int
        specify the position on the tetris board
        in terms of the square grid
    '''

    BLOCK_SIZE = 30
    OUTLINE_WIDTH = 2

  
    def __init__(self, pos, color):
        self.x = pos.x
        self.y = pos.y  

        p1 = Point(pos.x*Block.BLOCK_SIZE + Block.OUTLINE_WIDTH,
                   pos.y*Block.BLOCK_SIZE + Block.OUTLINE_WIDTH)
        p2 = Point(p1.x + Block.BLOCK_SIZE, p1.y + Block.BLOCK_SIZE) 
  
        Rectangle.__init__(self, p1, p2)
        #A Block is a special tyep of Rectangle
        #use this format to call the parent class Rectangle
        
        self.setWidth(Block.OUTLINE_WIDTH)
        self.setFill(color)
      

    def can_move(self, board, dx, dy): #Block.can_move
        ''' Parameters: dx - type: int
                        dy - type: int

            Return value: type: bool
                        
            checks if the block can move dx squares in the x direction
            and dy squares in the y direction
            Returns True if it can, and False otherwise
            HINT: use the can_move method on the Board object
        '''
        return board.can_move(self.x+dx, self.y+dy)

        #board.can_move checks if its parameters are within BOARD_WIDTH
        #and BOARD_HEIGHT
        
    
    def move(self, dx, dy):
        ''' Parameters: dx - type: int
                        dy - type: int
                        
            moves the block dx squares in the x direction
            and dy squares in the y direction
        '''

        self.x += dx
        self.y += dy
        #in other words, self.x = self.x + dx

        Rectangle.move(self, dx*Block.BLOCK_SIZE, dy*Block.BLOCK_SIZE)
