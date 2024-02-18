import pygame

# not used in the game but experiment with sprities
class PlayerSprite(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # self.image = pygame.image.load("falcon.jpg").convert()
        # self.rect = self.image.get_rect()

    def move(self, dx, dy):
        # print("move " + str(dx) + " " + str(dy))
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        # dy = dx
