import pygame
from pygame.sprite import Sprite

#This class will 
class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        super().__init__()
        self.screen = screen

        #Creating a bullet rect at (0,0) and then setting the correct position:
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Storing the bullet's position in order to modify it:
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        #Updating the decimal position of the bullet:
        self.y -= self.speed_factor
        #Updating the rect position:
        self.rect.y = self.y
    
    #This method will draw the bullet to the screen: 
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
        



