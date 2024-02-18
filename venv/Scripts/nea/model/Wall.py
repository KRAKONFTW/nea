import pygame

class Wall(object):
    def __init__(self, wx, wy, walls):
        walls.append(self)
        self.rect = pygame.Rect(wx, wy, 30, 30)

    # def reset_wall(self):
    #     self.active = False

    # def text_objects(text, font):
    #     textSurface = font.render(text, True, (255, 255, 255))
    #     return textSurface, textSurface.get_rect()
    #
    # def message_display(text, top, left, size, screen):
    #     # set font & size
    #     my_text = pygame.font.Font('freesansbold.ttf', size)
    #     # create text objets
    #     text_surface, text_rect = text_objects(text, my_text)
    #     # set where the text appears on screen
    #     text_rect.center = ((top)), (left)
    #     screen.blit(text_surface, text_rect)
