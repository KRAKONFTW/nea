import unittest

import sys
sys.path.append('../')

from classes.sprites.Enemy import *

class EnemyTest(unittest.TestCase):

        def test_enemy_position_should_move(self): #this function is used to test if the enemy's position should move
            walls = []
            # Create an instance of a Enemy and assert it's initial coordinates
            enemy = Enemy(walls)
            self.assertEqual(enemy.rect.x, 100)
            self.assertEqual(enemy.rect.y, 100)

            # Update the enemy coordinates by 10,20
            dx = 10
            dy = 20
            enemy.move_single_axis(dx,dy)
            self.assertEqual(enemy.rect.x, 110) #assert that the enemy's x coordinate is 110 because it has moved by 10
            self.assertEqual(enemy.rect.y, 120) #assert that the enemy's y coordinate is 120 because it has moved by 20



if __name__ == '__main__':
    unittest.main()
