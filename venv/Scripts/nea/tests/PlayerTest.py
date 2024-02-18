
import unittest,random

import sys
sys.path.append('../')

from model.Player import *
from model.LevelCreator import *
from model.MazeRenderer import *

class PlayerTest(unittest.TestCase):

    def test_initial_player_position(self):
        walls = []
        doors = []
        player = Player(walls, doors)
        player.move(10,10)
        self.assertEqual(player.rect.x, 50)
        self.assertEqual(player.rect.y, 50)

    def test_player_position_should_move(self):
        walls = []
        doors = []
        # Create an instance of a Player and assert it's initial coordinates
        player = Player(walls, doors)
        self.assertEqual(player.rect.x, 40)
        self.assertEqual(player.rect.y, 40)

        # Update the plauer coordinates by 10,20
        dx = 10
        dy = 20
        player.move_single_axis(dx,dy)
        self.assertEqual(player.rect.x, 50)
        self.assertEqual(player.rect.y, 60)

    def test_player_position_stops_at_wall(self):
        walls = []
        doors = []
        # Create all the levels
        levelCreator = LevelCreator()
        levels = levelCreator.create_levels()
        # Get a handle to the 1st level
        level = levels[0]

        # Build the walls using the level array
        maze_renderer = MazeRenderer(0,0)
        end_rect = maze_renderer.create_maze(level, walls, doors)
        # Create an instance of a Player and assert it's initial coordinates
        player = Player(walls, doors)
        self.assertEqual(player.rect.x, 40)
        self.assertEqual(player.rect.y, 40)

        # Update the plauer's x coordinate by -40 so that it would overlap with a wall
        dx = -40
        dy = 40
        player.move_single_axis(dx,dy)

        # The player's x coordinate should now be equal the right side of the wall
        self.assertEqual(player.rect.x, 30)
        # The player's y coordinate should now be equal the top side of the wall
        self.assertEqual(player.rect.y, 30)


if __name__ == '__main__':
    unittest.main()

