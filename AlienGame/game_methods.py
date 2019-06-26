import sys
import pygame
from bullet import Bullet

#This function will check for events from the user: 
def check_events(ai_settings, screen, ship, bullets):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_key_down(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_key_up(event, ship)

#This function will update the screen while the game is running: 
def update_screen(ai_settings, screen, ship, bullets):
    #Redrawing screen after each loop:
    screen.fill(ai_settings.game_color)

    #Redrawing the bullets on screen:
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.draw_ship()

    #Making most recently drawn screen visible:
    pygame.display.flip()


#Checking the keydown events:
def check_key_down(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

#Checking the keyup events:
def check_key_up(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_bullets(bullets):
    #Update the bullet's position:
    bullets.update()

     #Getting rid of bullets that have been fired for better memory management:
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)  

def fire_bullet(ai_settings, screen, ship, bullets):
    #Creating a new bullet and adding it to the bullets group:
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)




