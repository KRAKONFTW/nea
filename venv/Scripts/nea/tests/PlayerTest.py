
import unittest

import sys
sys.path.append('../')

from classes.sprites.Player import *
from classes.levels.LevelCreator import *
from classes.MazeRenderer import *

class PlayerTest(unittest.TestCase):
#this function is used to test the initial position of the player
    def test_initial_player_position(self):
        walls = []
        doors = [] #create an empty list of doors
        player = Player(walls, doors) #create an instance of a player and pass the list of walls and doors
        player.move(10,10)
        # assert that the player's x and y coordinate is 50
        self.assertEqual(player.rect.x, 50)
        self.assertEqual(player.rect.y, 50)

    def test_player_position_should_move(self): #this function is used to test if the player's position should move
        walls = []#create an empty list of walls which will be used to create the walls
        doors = []
        # Create an instance of a Player and assert it's initial coordinates
        player = Player(walls, doors)
        self.assertEqual(player.rect.x, 40) #assert that the player's x coordinate is 40
        self.assertEqual(player.rect.y, 40)

        # Update the player coordinates by 10,20
        dx = 10
        dy = 20
        player.move_single_axis(dx,dy) #move the player by 10,20
        self.assertEqual(player.rect.x, 50) #assert that the player's x coordinate as 50
        self.assertEqual(player.rect.y, 60) #assert that the player's y coordinate is 60

    def test_player_position_stops_at_wall(self): #this function is used to test if the player's position stops at the wall
        walls = [] #create an empty list of walls which will be used to create the walls in the level
        doors = []
        jewels = []
        # Create all the levels
        levelCreator = LevelCreator() #this is a class that is used to create the levels
        levels = levelCreator.create_levels()
        # Get a handle to the 1st level in the list of levels
        level = levels.dequeue() # get the first level in the list of levels

        # Build the walls using the level array
        maze_renderer = MazeRenderer(0,0) #create an instance of a maze renderer
        end_rect = maze_renderer.create_maze(level, walls, doors, jewels)
        # Create an instance of a Player and assert it's initial coordinates
        player = Player(walls, doors)
        self.assertEqual(player.rect.x, 40)
        self.assertEqual(player.rect.y, 40)

        # Update the player's x coordinate by -40 so that it would overlap with a wall
        dx = -40
        dy = 40
        player.move_single_axis(dx,dy) #move the player by -40,40

        # The player's x coordinate should now be equal the right side of the wall
        self.assertEqual(player.rect.x, 30)
        # The player's y coordinate should now be equal the top side of the wall
        self.assertEqual(player.rect.y, 30)


if __name__ == '__main__':
    unittest.main()

