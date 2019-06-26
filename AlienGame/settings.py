class Settings():
    #This is where all the settings will be stored for the game:

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.game_color = (230, 230, 230)

        #Bullet Settings:
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 0, 0

        #Ship settings:
        self.ship_speed_factor = 1.5