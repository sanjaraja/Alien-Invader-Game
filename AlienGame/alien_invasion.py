import pygame
import sys 
from settings import Settings
from ship import Ship
#from alien import Alien
import game_methods as game_runner
from pygame.sprite import Group
from game_stats import GameStats
from button import Button

#Making method that will start main loop of game:
def run_game():
    #Creating a screen object:
    pygame.init()
    pygame.display.set_caption("Alien Invader Game")
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    play_button = Button(ai_settings, screen, "Play")
    ship = Ship(ai_settings, screen)
    bullets = Group() 
    #alien = Alien(ai_settings, screen)
    aliens = Group()
    stats = GameStats(ai_settings)

    #Creating a fleet of aliens:
    game_runner.create_fleet(ai_settings, screen, ship, aliens)
    

    #This is the loop that will be running the game:
    while True:
        game_runner.check_events(ai_settings, screen, stats, play_button, ship, aliens,bullets)
        if stats.game_active:
                ship.update()
                game_runner.update_bullets(ai_settings, screen, ship, aliens, bullets)
                game_runner.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        game_runner.update_screen(ai_settings, screen, stats, ship, aliens, bullets, play_button)

run_game()