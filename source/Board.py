
import numpy as np


#represents the board and makes changes to it and get information about the Board
#the board will be (nxn) (row x column)
#   0 reps an empty square
#   1 reps player one square
#   2 reps player two square
class Board:

    #size is how big the board is (board x board)
    #size must be greater than 2 and even
    def __init__(self, size = 8):
        self.board = np.zeros((size,size))


    #initilizes the board
    #assume the board is completely empty
    #   the size of the board is (nxn) where n > 2 and even
    #changes self.board
    #   the upper right middle place will be =1
    #   the upper left middle place will be = 2
    #   the lower right middle place will be = 2
    #   the lower left middle place will be = 1
    #   the rest of the board will = 0
    def InitilizeBoard(self):
        #TODO danielle: you can do it
        #delete the line below this
        pass