import pygame

class Door(object):
    def __init__(self, wx, wy, doors):
        doors.append(self)
        self.rect = pygame.Rect(wx, wy, 30, 30)

    def reset_door(self):
        self.active = True

    def is_active(self):
        return self.active