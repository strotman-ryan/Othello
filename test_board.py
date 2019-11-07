

import unittest
from source.Board import Board
import numpy as np


class TestBoardConstructor(unittest.TestCase):

    def test_size_3(self):
        exp_board = Board(4).board
        test_board = np.array([[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]])
        self.assertTrue(np.array_equal(exp_board, test_board))

class TestBoardInitilitazion(unittest.TestCase):

    def test_initialize_size_4(self):
        exp_board_obj = Board(4)
        exp_board_obj.InitilizeBoard()
        exp_board = exp_board_obj.board

        test_board = Board(4).board
        test_board[1,1] = 2
        test_board[1,2] = 1
        test_board[2,1] = 1
        test_board[2,2] = 2
        self.assertTrue(np.array_equal(exp_board, test_board))


if __name__ == '__main__':
    unittest.main()