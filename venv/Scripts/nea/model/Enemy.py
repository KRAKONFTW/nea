import pygame

class Enemy(object):

    def __init__(self, walls):
        self.rect = pygame.Rect(100, 100, 60, 60)
        self.walls = walls
        self.last_moved = "N"

    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)

    # changes the position of the x and y position
    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        for wall in self.walls:
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom
        # dy = dx

    def wander(self):
        if self.last_moved == "N":
            self.move(0, -5)
            # print("move north")
        else:
            self.move(0, 5)
            # print("move south")
