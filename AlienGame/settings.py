class Settings():
    #This is where all the settings will be stored for the game:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.game_color = (230, 230, 230)

        #Bullet Settings:
        #self.bullet_speed_factor = 1.5
        self.bullet_width = 7
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0
        self.bullets_allowed = 4

        #Ship settings:
        #self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #Alien Settings:
        #self.alien_speed_factor = 1
        self.fleet_drop_speed = 10 #This variable will keep track of how quickly the fleet will drop
        #Can switch the fleet_direction value between 1 and -1 to indicate which way the alien fleet will move
        #self.fleet_direction = 1

        #How quickly the game will speed up:
        self.speedup_scale_aliens = 1.3
        self.speedup_scale_player = 1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #These attributes will change throughout the game
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1

        #fleet direction:
        self.fleet_direction = 1
    
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale_player
        self.bullet_speed_factor *= self.speedup_scale_player
        self.alien_speed_factor *= self.alien_speed_factor


