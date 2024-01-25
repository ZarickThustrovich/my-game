from shortcuts import get_path_plus_name
from settings import (
  SPRITES_PATH,
  RESOLUTION,
)

class Background:
    def __init__(self, path:str, pygame):
        self.width = RESOLUTION[0]
        self.height = RESOLUTION[1]
        self.path = path
        self.pygame = pygame
        self.sheet = self.load_image_and_convert(path)
    
    def load_image_and_convert(self, filename):
        return self.pygame.image.load(filename).convert_alpha()
    
    def get(self):
        sprite = self.pygame.Surface([self.width, self.height], self.pygame.SRCALPHA)
        y = 0
        x = 0
        sprite.blit(self.sheet, (0, 0), (x, y, self.width, self.height))
        return sprite
