import sys
import pygame

#This function will check for events from the user: 
def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

#This function will update the screen while the game is running: 
def update_screen(ai_settings, screen ,ship):
    #Redrawing screen after each loop:
    screen.fill(ai_settings.game_color)
    ship.draw_ship()

    #Making most recently drawn screen visible:
    pygame.display.flip()

