import pygame
import sys 
from settings import Settings
from ship import Ship
import game_methods as game_runner

#Making method that will start main loop of game:
def run_game():
    #Creating a screen object:
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    ship = Ship(screen)
    

    #This is the loop that will be running the game:
    while True:
        game_runner.check_events(ship)
        ship.update()
        game_runner.update_screen(ai_settings, screen, ship)

run_game()