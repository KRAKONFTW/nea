import pygame

class Wall(object):
    def __init__(self, wx, wy, walls):
        walls.append(self)
        self.rect = pygame.Rect(wx, wy, 30, 30)
        self.image = pygame.image.load('resources/wall3.png')
