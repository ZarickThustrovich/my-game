from shortcuts import get_path_plus_name
from settings import SPRITES_PATH


class Texture:
    def __init__(self, width:int, height:int, path:str, pygame):
        self.width = width
        self.height = height
        self.path = path
        self.pygame = pygame
        self.sheet = self.load_image_and_convert(path)
        self.reversed = reversed
    
    def load_image_and_convert(self, filename):
        return self.pygame.image.load(filename).convert_alpha()
    
    def get(self):
        texture_rect = self.pygame.Surface((16, 16), self.pygame.SRCALPHA)
        texture_rect.blit(self.sheet, (0, 0))
        # sprite = self.pygame.Surface([self.width, self.height], self.pygame.SRCALPHA)
        # y = 0
        # x = 0
        # sprite.blit(self.sheet, (0, 0), (x, y, self.width, self.height))
        return self.pygame.transform.scale(texture_rect, (self.width, self.height))
