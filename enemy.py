class Enemy:
    def __init__(self, pygame, screen, spritesheet, genus):
        self.genus = genus
        self.spritesheet = spritesheet
        self.pygame = pygame
        self.screen = screen
        self.x = 700 - 100
        self.y = 700 - 50
        
    def spawn(self):
        self.image = self.spritesheet(self.width, self.height, 'idle_1', reversed, self.actions_counter['idle'], 4)
        sprite = self.image.get_sprite()
        self.screen.blit(sprite, (self.x, self.y, self.width, self.height))
        self.pygame.display.flip()
    
    def attack(self):
        return 0

    def move_to_player(self, player_x):
        if player_x < self.x:
            self.x - 10
        elif player_x > self.x:
            self.x + 10
        else:
            self.attack()

    
    