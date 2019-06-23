import pygame
import sys 

#Making method that will start main loop of game:
def run_game():
    #Creating a screen object:
    pygame.init()
    screen = pygame.display.set_mode((1100, 700))
    game_color = (192, 192, 192)

    #This is the loop that will be running the game:
    while True:

        #Looking for keyboard and mouse events in gameL:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        #Redrawing the screen after each pass through loop:
        screen.fill(game_color)
        
        #This will ensure that the drawing screen will be there:
        pygame.display.flip()

run_game()