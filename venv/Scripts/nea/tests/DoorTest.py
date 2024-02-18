import unittest

import sys
sys.path.append('../')

from model.Door import *

class DoorTest(unittest.TestCase):

    def test_reset_door(self):
        doors = []
        wx = 0
        wy = 0
        door = Door(wx, wy, doors)
        door.reset_door()
        self.assertEqual(door.is_active(), True)

if __name__ == '__main__':
    unittest.main()

