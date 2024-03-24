from classes.sprites.Door import *
from classes.sprites.Wall import *
from classes.sprites.Jewel import *

class MazeRenderer(object):
    def __init__(self, x, y ):
        print('Calling self.rect')
        self.rect = pygame.Rect(x, y, 30, 30)

    def create_maze(self, level, walls, doors, jewels):
        x = y = 0
        for row in level.level_map:
            for col in row:  # for character in row
                if col == "W":  # if the character is = to w, then create a wall
                    Wall(x, y, walls)  # creating a wall object and pass the list of walls
                if col == "Q":
                    Door(x, y, doors)
                if col == "E":
                    rect = pygame.Rect(x, y, 30, 30)  # initialising a variable called end_rect.
                    # this is used to denote the end of the level (red box)
                if col == "J":
                    Jewel(x, y, jewels)
                x += 30  # increments x and y through each iteration through the loop.
            y += 30
            x = 0
        return rect