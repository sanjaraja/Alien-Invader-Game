import sys
import pygame
from bullet import Bullet
from alien import Alien

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
def update_screen(ai_settings, screen, ship, aliens, bullets):
    #Redrawing screen after each loop:
    screen.fill(ai_settings.game_color)

    #Redrawing the bullets on screen:
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.draw_ship()
    aliens.draw(screen)

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
    elif event.key == pygame.K_q:
        sys.exit()

#Checking the keyup events:
def check_key_up(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_bullets(ai_settings, screen, ship, aliens, bullets):
    #Update the bullet's position:
    bullets.update()

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)

     #Getting rid of bullets that have been fired for better memory management:
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)  

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    #Check if the bullet has made contact with an alien. If so, need to get rid of bullet and alien:
    collisions = pygame.sprite.groupcollide(bullets, aliens, False, True)

    if len(aliens) == 0:
        bullets.empty() 
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    #Creating a new bullet and adding it to the bullets group:
        if len(bullets) < ai_settings.bullets_allowed:
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def create_fleet(ai_settings, screen, ship, aliens):
    #Create an alien and find how many aliens can fit in a row of aliens:
    #Spacing between each alien will be one alien width:

    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    #Creating a row of aliens:
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)
    

def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)

def get_number_rows(ai_settings, ship_height, alien_height):
    #First need to determine how many rows of aliens can fit onto the screen:
    available_space_y = (ai_settings.screen_height - (3 * alien_height)- ship_height)
    number_rows = int(available_space_y/(2 * alien_height))
    return number_rows

#This method calls method in alien class to make row of aliens move:
def update_aliens(ai_settings, ship, aliens):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    #Looking for ship and alien collissions:
    if pygame.sprite.spritecollideany(ship, aliens):
        print("The ship has been hit")

#This method will check if an alien has reached the edge and will make the fleet of aliens change direction if so:
def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    #Drops alien fleet down and changes the direction the alien fleet is moving in:
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    
    ai_settings.fleet_direction *= -1



