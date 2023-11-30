class Background:
    def __init__(self, pygame, screen, spritesheet, genus):
        self.genus = genus
        self.spritesheet = spritesheet
        self.pygame = pygame
        self.screen = screen
        self.x = 700 - 100
        self.y = 700 - 50
        
    def appear(self):
        self.image = self.spritesheet(self.width, self.height, 'background-sprite-name', False, self.actions_counter['idle'], 4)
        sprite = self.image.get_sprite()
        self.screen.blit(sprite, (self.x, self.y, self.width, self.height))
        self.pygame.display.flip()
    

    
    