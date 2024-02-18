import pygame
from model.Wall import *
from model.Door import *

def create_maze(level, walls, doors, end_rect):
    x = y = 0
    for row in level:
        print('xxx')
        for col in row:
            if col == "W":
                Wall(x, y, walls)
            if col == "Q":
                Door(x, y, doors)
            if col == "E":
                print('end_rect')
                # global end_rec
                end_rect = pygame.Rect(x, y, 30, 30)
            x += 30
        y += 30
        x = 0