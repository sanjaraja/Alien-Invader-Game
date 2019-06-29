import pygame.font
class Scoreboard():
    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.ai_settings = ai_settings
        self.screen_rect = screen.get_rect()
        self.stats = stats
        #self.score = 11

        #These are the font settings for storing scoring information:
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        #Preparing the initial score image:
        self.prep_score()
        self.prep_high_score()
    
    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1)) #This will round the score to the nearest 10
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.ai_settings.game_color)

        #Displaying the score on the top right corner of the window:
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        #Drawing the score to the screen:
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
    
    def prep_high_score(self):
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, self.ai_settings.game_color)

        #Need to center the high score at the top of the screen:
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top
