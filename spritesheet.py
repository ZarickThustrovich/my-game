import os


SPRITES_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sprites')


class SpriteSheet:
    def __init__(self, width:int, height:int, state:str, reversed:bool, accelerate:int, divider:int, pygame):
        self.width = width
        self.height = height
        self.state = state
        self.sheet = pygame.image.load(os.path.join(SPRITES_PATH, f"{state}.png")).convert_alpha()
        self.reversed = reversed
        self.accelerate = accelerate
        self.divider = divider
        self.pygame = pygame
    
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