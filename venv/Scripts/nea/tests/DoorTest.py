import unittest

import sys
sys.path.append('../')

from classes.sprites.Door import *

class DoorTest(unittest.TestCase):

    def test_reset_door(self):
        doors = []
        wx = 10
        wy = 20
        door = Door(wx, wy, doors)
        door.reset_door()
        self.assertEqual(door.is_active(), True)
        self.assertEqual(door.rect.x, 10)
        self.assertEqual(door.rect.y, 20)
        self.assertEqual(door.rect.width, 30)
        self.assertEqual(door.rect.height, 30)

if __name__ == '__main__':
    unittest.main()

