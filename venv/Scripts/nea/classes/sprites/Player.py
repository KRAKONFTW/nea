import pygame

class Player(object):

    def __init__(self, walls, doors):
        self.rect = pygame.Rect(40, 40, 30, 30)
        self.image = pygame.image.load('resources/Player.png')
        self.walls = walls
        self.doors = doors

    # move the player object by dx across the x-axis or dy across the y-axis
    def move(self, dx, dy):
        if dx != 0:
            self.move_single_axis(dx, 0)
        if dy != 0:
            self.move_single_axis(0, dy)
    # changes the position of the x and y position
    def move_single_axis(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
        for wall in self.walls:  # block the players position if it collides with a wall
            if self.rect.colliderect(wall.rect):
                if dx > 0:
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom
        for door in self.doors:
            if self.rect.colliderect(door.rect):
                if dx > 0:
                    self.rect.right = door.rect.left
                if dx < 0:
                    self.rect.left = door.rect.right
                if dy > 0:
                    self.rect.bottom = door.rect.top
                if dy < 0:
                    self.rect.top = door.rect.bottom

