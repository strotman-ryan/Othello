

import source.Game as Game

import unittest



class TestAdd(unittest.TestCase):

    def test_1_1(self):
        self.assertEqual(Game.add(1,1), 2)

    def test_1_2(self):
        self.assertEqual(Game.add(1,2),3)


if __name__ == '__main__':
    unittest.main()
