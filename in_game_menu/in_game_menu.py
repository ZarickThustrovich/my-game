from settings import (
    RESOLUTION, 
    SURFACE_BOTTOM_BORDER,
    PLAYER_HEALTH,
)



class InGameMenu:
    def __init__(self, pygame, screen, player_health):
        self.pygame = pygame
        self.screen = screen
        self.player_health = player_health
        self.width = RESOLUTION[0]
        self.height = RESOLUTION[1] - SURFACE_BOTTOM_BORDER
        self.x = 0
        self.y = RESOLUTION[1] - self.height
        self.hp_bar = HPbar(self.pygame, self.screen, self.width, self.height, self.player_health)
    
    def reveal(self):
        color = (166, 176, 62)
        self.pygame.draw.rect(self.screen, color, (self.x, self.y, self.width, self.height))
        self.hp_bar.reveal()
        # self.pygame.display.flip()
        
        
class HPbar():
    def __init__(self, pygame, screen, menu_width, menu_height, player_health):
        self.pygame = pygame
        # self.width = menu_width // 2 - 50
        self.width = player_health
        self.player_health = player_health
        self.height = menu_height // 3
        self.screen = screen
        self.x = 20
        self.y = RESOLUTION[1] - self.height
    
    def reveal(self):
        color = (255,0,0)
        self.pygame.draw.rect(self.screen, color, (self.x, self.y, self.width, self.height))
        
    