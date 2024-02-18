import pygame, sys, random
from pygame.locals import QUIT

from model.Door import *
from model.Player import *
from model.Enemy import *
from model.EnemySprite import *
from model.PlayerSprite import *
from model.Wall import *
from model.MazeRenderer import *
from model.LevelCreator import *

pygame.init()

pygame.display.set_caption('Welcome to knockoff geometry dash!')
width = 620
height = 540
screen = pygame.display.set_mode((width, height))
colour = (0, 128, 255)
move = (0, random)
last_moved = 0
clock = pygame.time.Clock()
walls = []
doors = []
end_rect = pygame.Rect(0, 0, 0, 0)
player = Player(walls, doors)
enemy = Enemy(walls)
enemy_sprite = Enemy_Sprite()
player_sprite = PlayerSprite()  # Creates a player sprite
wall_colour = (255, 255, 255)  # the colour is set up as white to start with

levelCreator = LevelCreator()
levels = levelCreator.create_levels()
level = random.choice(levels)

# Build the walls using the level array
# end_rect = create_maze(level, walls, doors)
maze_renderer = MazeRenderer(0,0)
end_rect = maze_renderer.create_maze(level, walls, doors)


while True:  # main loops inside of the game
    clock.tick(60)  # used to slow down the program
    for event in pygame.event.get():  # checks if user pressed escape
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    x = random.randint(0, 1)
    enemy.move(x, 5)
    enemy.wander()
    user_input = pygame.key.get_pressed()  # moves the player around
    if user_input[pygame.K_UP]:
        player.move(0, -5)
    elif player.rect.y < (height - 60):
        player.move(0, 5)
    if user_input[pygame.K_DOWN]:
        player.move(0, 5)
    if user_input[pygame.K_LEFT]:
        player.move(-5, 0)
        if player.rect.x < 0:
            player.rect.x = width - 1
    if user_input[pygame.K_RIGHT]:
        player.move(5, 0)
        if player.rect.x > width:
            player.rect.x = -59

    # if the player collides with the red box, You delete the level
    if player.rect.colliderect(end_rect):
        del walls[:]  # this deletes the contents of the walls array
        level = random.choice(levels)  # picks a random level
        # picks a random colour
        wall_colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    if player.rect.colliderect(end_rect):
        del doors[:]

        # creating the background
        end_rect = maze_renderer.create_maze(level, walls, doors)

    screen.fill((0, 0, 0))
    for wall in walls:
        pygame.draw.rect(screen, wall_colour, wall.rect)  # randomly generates different coloured walls
    for door in doors:
        pygame.draw.rect(screen, (32, 178, 170), door.rect)
        # pygame.draw.rect(screen, (0,0,0), wall.rect)
    pygame.draw.rect(screen, (255, 0, 0), end_rect)
    pygame.draw.rect(screen, colour, player.rect)
    pygame.draw.rect(screen, (128, 0, 32), enemy.rect)

    pygame.display.update()




