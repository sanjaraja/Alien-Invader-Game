import pygame

class Ship():
    def __init__ (self, screen):
        self.screen = screen

        #Generating the ship within the game:
        self.image = pygame.image.load("AlienGame/images/ship.bmp")
        self.rect = self.image.get_rect() #Making the image a rectangle to easily access the coordinates and movement
        self.screen_rect = screen.get_rect()

        #Starting the ship at a defined position:
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Directional movement flags:
        self.moving_right = False
        self.moving_left = False


    #This method will allow for the ship to be actually drawn
    def draw_ship(self):
        self.screen.blit(self.image, self.rect)

    #This method will update the position of the ship:
    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        elif self.moving_left:
            self.rect.centerx -= 1