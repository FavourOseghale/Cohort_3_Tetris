"""The Block class represents a Tetris block with an ID, rotation states, cell positions, and methods for moving,
rotating, and drawing the block on a Pygame screen."""


from graphics import *
import random

class Block_Class(Rectangle):

    BLOCK_SIZE = 30
    OUTLINE_WIDTH = 2

  
    def __init__(self, pos, color):
        self.x = pos.x
        self.y = pos.y  

        p1 = Point(pos.x*Block_Class.BLOCK_SIZE + Block_Class.OUTLINE_WIDTH,
                   pos.y*Block_Class.BLOCK_SIZE + Block_Class.OUTLINE_WIDTH)
        
        p2 = Point(p1.x + Block_Class.BLOCK_SIZE, p1.y + Block_Class.BLOCK_SIZE) 
  
        Rectangle.__init__(self, p1, p2)
        
        self.setWidth(Block_Class.OUTLINE_WIDTH)
        self.setFill(color)
      

    def can_move(self, board, dx, dy): #Block.can_move
        return board.can_move(self.x+dx, self.y+dy)

    
    def move(self, dx, dy)
        self.x += dx
        self.y += dy

        Rectangle.move(self, dx*Block_Class.BLOCK_SIZE, dy*Block_Class.BLOCK_SIZE)
