import unittest

import sys
sys.path.append('../')

from model.Wall import *

class WallTest(unittest.TestCase):

    def test_objects(self):
        walls = []
        dx = 0
        dy = 0
        wall = Wall(dx, dy, walls)
        wall.text_objects()

        text = "aaa"
        font =
        wall = font.render(text, font)
        font.render()
        wall.text_objects()



if __name__ == '__main__':
    unittest.main()

