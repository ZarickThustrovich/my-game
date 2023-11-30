from shortcuts import get_path_plus_name
from settings import SPRITES_PATH


class SpriteSheet:
    def __init__(self, width:int, height:int, state:str, reversed:bool, accelerate:int, divider:int, pygame):
        self.width = width
        self.height = height
        self.state = state
        self.pygame = pygame
        self.sheet = self.load_image_and_convert(f'{state}.png')
        self.reversed = reversed
        self.accelerate = accelerate
        self.divider = divider
    
    def load_image_and_convert(self, filename):
        return self.pygame.image.load(get_path_plus_name(SPRITES_PATH, filename)).convert_alpha()
    
    def get_sprite(self):
        sprite = self.pygame.Surface([self.width, self.height], self.pygame.SRCALPHA)
        y = 0
        if self.reversed:
            reversed_by_divider = [i for i in range(0, self.divider)]
            reversed_x = reversed_by_divider[self.accelerate - 1]
            x = reversed_x * self.width
            sprite.blit(self.pygame.transform.flip(self.sheet, True, False), (0, 0), (x, y, self.width, self.height))
        else:
            x = self.accelerate * self.width
            sprite.blit(self.sheet, (0, 0), (x, y, self.width, self.height))
        print('x,y=', x, y)
        return sprite