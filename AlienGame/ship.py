import pygame

class Ship():
    def __init__ (self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

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

        #Decimal Value for ship's center:
        self.center = float(self.rect.centerx)



    #This method will allow for the ship to be actually drawn
    def draw_ship(self):
        self.screen.blit(self.image, self.rect)

    #This method will update the position of the ship:
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        #Updating the rect object:
        self.rect.centerx = self.center