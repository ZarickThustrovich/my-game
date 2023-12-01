from settings import (
    RESOLUTION,
    BUTTONS,
)



class Menu:
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen
        self.color = (0, 100, 0)
        self.width = RESOLUTION[0] // 2
        self.height = RESOLUTION[1] // 2
        self.font = self.pygame.font.Font(None, 24)
        self.x = RESOLUTION[0] // 2 + self.width
        self.y = RESOLUTION[1] // 2 + self.height
            
    def reveal(self):
        self.pygame.draw.rect(self.screen, self.color, (self.x, self.y, self.width, self.height))
        self.pygame.display.update()
        
    def reveal_buttons(self):
        width = self.width // 2
        height = self.height // 3
        start_x = self.width // 2 + width // 2
        start_y = self.y // 2 + height // 2
        color = (255, 0, 0)
        for button_name in BUTTONS:
            button_surface = self.pygame.Surface([width, height], self.pygame.SRCALPHA)
            text = self.font.render(button_name, True, (180, 0, 0))
            button_surface.blit(text, (start_x, start_x), (start_x, start_y, width, height))
            # self.pygame.draw.rect(self.screen, color, (start_x, start_y, width, height))
            start_y -= 100
        self.pygame.display.update()
        