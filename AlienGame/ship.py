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


    #This method will allow for the ship to be actually drawn
    def blitme(self):
        self.screen.blit(self.image, self.rect)