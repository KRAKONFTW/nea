import pygame, math

class Enemy(object): #This class is used to create the enemy object
# This class is used to create the enemy object
    def __init__(self, walls, player): #This initialises the enemy object and takes in the walls parameter

        self.rect = pygame.Rect(player.rect.x + 200, player.rect.y + 200, 60, 60) #This line creates a rectangle object for the enemy and sets its x and y coordinates to 100 and 100 respectively and its width and height to 60 and 60 respectively
        self.image = pygame.image.load('resources/Enemy.png')
        self.walls = walls  #This line initialises the walls attribute to the walls parameter
        self.last_moved = "N" #This line initialises the last_moved attribute to "N"

    def move(self, dx, dy): #This function is used to move the enemy object by dx across the x-axis o
        if dx != 0:
            self.move_single_axis(dx, 0) #This line calls the move_single_axis function and passes in the dx and 0 parameters
        if dy != 0:#This line checks if the dy parameter is not equal to 0
            self.move_single_axis(0, dy)

    # changes the position of the x and y position
    def move_single_axis(self, dx, dy):
        self.rect.x += dx #This line adds the dx parameter to the x coordinate of the enemy object
        self.rect.y += dy
        for wall in self.walls: #This line iterates through the walls list
            if self.rect.colliderect(wall.rect): #This line checks if the enemy object collides with a wall object
                if dx > 0: #This line checks if the dx parameter is greater than 0
                    self.rect.right = wall.rect.left
                if dx < 0:
                    self.rect.left = wall.rect.right
                #This line sets the left of the enemy object to the right of the wall object
                if dy > 0:
                    self.rect.bottom = wall.rect.top
                if dy < 0:
                    self.rect.top = wall.rect.bottom
                #This line sets the top of the enemy object to the bottom of the wall object


    def follow_player(self, player): #This function is used to make the enemy object follow the player object
        #This line checks if the x coordinate of the enemy object is less than the x coordinate of the player object
        if self.rect.x < player.rect.x:
            self.move(5, 0)
            self.last_moved = "E" #This line sets the last_moved attribute to "E"
            # print("move east")
        elif self.rect.x > player.rect.x: #
            self.move(-5, 0) #This line moves the enemy object by -5 across the x-axis
            self.last_moved = "W"
            # print("move west")
        elif self.rect.y < player.rect.y: #
            self.move(0, 5) #This line moves the enemy object by 5 across the y-axis
            self.last_moved = "S"
            # print("move south")
        elif self.rect.y > player.rect.y:
        #This line checks if the y coordinate of the enemy object is greater than the y coordinate of the player object
            self.move(0, -5)
            self.last_moved = "N"
            # print("move north")

    def move_towards_player(self, player, speed):
        # Find direction vector (dx, dy) between enemy and player.
        self.speed = speed
        dx, dy = player.rect.x - self.rect.x, player.rect.y - self.rect.y
        dist = math.hypot(dx, dy)
        if dist != 0:
            dx, dy = dx / dist, dy / dist  # Normalize.
        # Move along this normalized vector towards the player at current speed.
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        if self.rect.colliderect(player.rect):
            # Enemy collided with Player
            return True
        else:
            return False

        # for wall in self.walls:  # change the enemy's position if it collides with a wall
        #     if self.rect.colliderect(wall.rect):
        #         if dx > 0:
        #             self.rect.right = wall.rect.left
        #         if dx < 0:
        #             self.rect.left = wall.rect.right
        #         if dy > 0:
        #             self.rect.bottom = wall.rect.top
        #         if dy < 0:
        #             self.rect.top = wall.rect.bottom

    # Same thing using only pygame utilities
    def move_towards_player2(self, player):
        # Find direction vector (dx, dy) between enemy and player.
        dirvect = pygame.math.Vector2(player.rect.x - self.rect.x,
                                      player.rect.y - self.rect.y)
        if dirvect.length_squared() > 0:
            dirvect.normalize()
        # Move along this normalized vector towards the player at current speed.
        if dirvect.length_squared() > 0:
            dirvect.scale_to_length(self.speed)
        self.rect.move_ip(dirvect)

        