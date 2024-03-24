import pygame

class Jewel(object):
    def __init__(self, wx, wy, jewels):
        jewels.append(self)
        self.rect = pygame.Rect(wx, wy, 30, 30)
        self.image = pygame.image.load('resources/jewel.png')

