import unittest

import sys
sys.path.append('../')

from classes.sprites.Wall import *

class WallTest(unittest.TestCase):

    def test_objects(self):
        walls = []
        dx = 0
        dy = 0
        wall = Wall(dx, dy, walls)
        self.assertEqual(wall.rect.x, 0)


if __name__ == '__main__':
    unittest.main()

