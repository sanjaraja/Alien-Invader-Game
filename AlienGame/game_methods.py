import sys
import pygame

#This function will check for events from the user: 
def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event, ship)
        elif event.type == pygame.KEYUP:
            check_key_up(event, ship)

#This function will update the screen while the game is running: 
def update_screen(ai_settings, screen ,ship):
    #Redrawing screen after each loop:
    screen.fill(ai_settings.game_color)
    ship.draw_ship()

    #Making most recently drawn screen visible:
    pygame.display.flip()

#Checking the keydown events:
def check_key_down(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True

#Checking the keyup events:
def check_key_up(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False



