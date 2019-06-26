import pygame
from pygame.sprite import Sprite

#This class represents a single alien:
class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        """Need to initialize the initial starting position of the alien"""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        #Creating the alien image and setting its rect properties:
        self.image = pygame.image.load("AlienGame/images/alien.bmp")
        self.rect = self.image.get_rect()

        #Starting the alien near the top left corner of screen:
        self.rect.x = self.rect.width 
        self.rect.y = self.rect.height

        #Storing the alien's position:
        self.x = float(self.rect.x)
    
    def draw_alien(self):
        self.screen.blit(self.image, self.rect)

