import pygame
import sys 
from settings import Settings
from ship import Ship
#from alien import Alien
import game_methods as game_runner
from pygame.sprite import Group

#Making method that will start main loop of game:
def run_game():
    #Creating a screen object:
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(ai_settings, screen)
    bullets = Group() 
    #alien = Alien(ai_settings, screen)
    aliens = Group()

    #Creating a fleet of aliens:
    game_runner.create_fleet(ai_settings, screen, ship, aliens)
    

    #This is the loop that will be running the game:
    while True:
        game_runner.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        game_runner.update_bullets(ai_settings, screen, ship, aliens, bullets)
        game_runner.update_aliens(ai_settings, aliens)
        game_runner.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()