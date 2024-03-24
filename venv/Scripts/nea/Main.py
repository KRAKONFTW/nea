import sys, random
from pygame.locals import *
from pygame.locals import QUIT

from classes.sprites.Player import *
from classes.sprites.Enemy import *
from classes.MazeRenderer import *
from classes.levels.LevelCreator import *
from data_access_layer.HighScoreRepository import *
from classes.GameContext import *
from classes.button import Button

pygame.init()

screen = pygame.display.set_mode((900, 700))
pygame.display.set_caption('Menu')
BG = pygame.image.load("resources/MenuBackground.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("resources/font.ttf", size)

def play(game_context):
    pygame.display.set_caption('Phantom Dungeons')
    width = 900
    height = 700
    screen = pygame.display.set_mode((width, height))
    colour = (0, 128, 255)
    clock = pygame.time.Clock()
    walls = []
    doors = []
    jewels = []
    player = Player(walls, doors)
    playerInventory = game_context.get_player_inventory()
    enemy = Enemy(walls, player)

    levelCreator = LevelCreator()
    level_queue = levelCreator.create_levels()
    level = level_queue.dequeue()

    # Build the walls using the level array
    # end_rect = create_maze(level, walls, doors)
    maze_renderer = MazeRenderer(0,0)
    end_rect = maze_renderer.create_maze(level, walls, doors, jewels)
    pygame.display.set_caption(level.level_name)


    while True:  # main loops inside of the game
        clock.tick(60)  # used to slow down the program
        for event in pygame.event.get():  # checks if user pressed escape
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        x = random.randint(0, 5)
        enemy_collision = enemy.move_towards_player(player, 1)
        if enemy_collision:
            print("You died")
            break
        # enemy.move_towards_player2(player)
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
            level = level_queue.dequeue() # get the next level in the level queue
            # picks a random colour
            wall_colour = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        if player.rect.colliderect(end_rect):
            del doors[:]

            # creating the background
            end_rect = maze_renderer.create_maze(level, walls, doors, jewels)
            pygame.display.set_caption(level.level_name)

        screen.fill((0, 0, 0))

        for wall in walls:
            screen.blit(wall.image, wall.rect) # draws each wall on the screen

        for door in doors:
            screen.blit(door.image, door.rect) # draws each door on the screen

        for jewel in jewels:
            screen.blit(jewel.image, jewel.rect) # draws each jewel on the screen
            if player.rect.colliderect(jewel.rect): # if the player collides with a jewel
                transparent = (0, 0, 0, 0) # make the jewel transparent
                jewel.image.fill(transparent)
                screen.blit(jewel.image, jewel.rect)
                playerInventory.add_jewel(jewel)    # add the jewel to the player's inventory
                jewels.remove(jewel) # remove the jewel from the list of jewels

        pygame.draw.rect(screen, (255, 0, 0), end_rect)
        screen.blit(player.image, player.rect)
        # pygame.draw.rect(screen, (128, 0, 32), enemy.rect)
        screen.blit(enemy.image, enemy.rect)

        pygame.display.update()

    player_died()

    show_score(game_context)

def quit():
    pygame.quit()
    sys.exit()

def player_died():
    while True:
        playerDeathBg = pygame.image.load("resources/PlayerDeathBackground.png")
        screen.blit(playerDeathBg, (0, 0))
        MENU_TEXT = get_font(50).render("You Died!", True, "#D7D882")
        MENU_RECT = MENU_TEXT.get_rect(center=(430, 100))
        screen.blit(MENU_TEXT, MENU_RECT)
        pygame.display.update()
        pygame.event.wait()
        break

def show_score(game_context):
    totalJewels = game_context.get_player_inventory().get_total_items()
    print("Player Name: " + game_context.get_player_name() + ", Total jewels: " + str(totalJewels))
    write_highscore_to_file("../high_score.csv", game_context.get_player_name(), totalJewels)
    render_highscore()
    main_menu()

def render_highscore():
    high_scores = read_highscore_from_file("../high_score.csv")
    print("High Scores: ")
    for player_name, score in high_scores.items():
        print(player_name + " " + str(score))

    high_score_bg = pygame.image.load("resources/HighScoreBackground.png")
    pygame.display.set_caption("High Scores")
    sorted_scores = dict(sorted(high_scores.items(), key=lambda item: item[1], reverse=True))

    while True:
        screen.blit(high_score_bg, (0, 0))
        render_text("High Scores", 300, 100,30)

        for i, (player_name, score) in enumerate(sorted_scores.items()):
            render_text(f"{player_name}: {score}", 300, 170 + i * 50)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                main_menu()

def render_text(word, x, y, font_size=15):
    font =get_font(font_size)
    text = font.render("{}".format(word), True, "#D7D882")
    return screen.blit(text,(x,y))

def enter_player_name():
    clock = pygame.time.Clock()
    screen.blit(BG, (0, 0))
    player_name = ""
    input_box = pygame.Rect(400, 200, 1000, 30)
    render_text("Please enter thy name: ", 75, 200)  # example asking name
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    done = False
                else:
                    player_name += event.unicode
            txt_surface = get_font(15).render(player_name, True, "#D7D882")
            width = 400
            input_box.w = width
            # Blit the text.
            screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))

            pygame.display.flip()
            clock.tick(60)

    return player_name

def main_menu():
    while True:
        screen.blit(BG, (0, 0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(50).render("Phantom Dungeons ", True, "#D7D882")
        menu_rect = menu_text.get_rect(center=(450, 100))

        play_button = Button(image=pygame.image.load("resources/Play Rect.png"), pos=(435, 200),
                             text_input="Play", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
        high_scores_button = Button(image=pygame.image.load("resources/Play Rect.png"), pos=(435, 320),
                                text_input="High Score", font=get_font(20), base_color="#d7fcd4", hovering_color="White")
        quit_button = Button(image=pygame.image.load("resources/Play Rect.png"), pos=(435, 440),
                             text_input="Quit", font=get_font(20), base_color="#d7fcd4", hovering_color="White")

        screen.blit(menu_text, menu_rect)

        for button in [play_button, high_scores_button, quit_button]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.checkForInput(menu_mouse_pos):
                    player_name = enter_player_name()

                    game_context = GameContext(player_name)
                    play(game_context)
                if high_scores_button.checkForInput(menu_mouse_pos):
                    render_highscore()
                if quit_button.checkForInput(menu_mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()


