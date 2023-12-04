from settings import (
    RESOLUTION,
    SURFACE_BOTTOM_BORDER,
)
from random import randint


class Surface:
    def __init__(self, pygame, screen, genus):
        self.genus = genus
        self.block_width = 20
        self.pygame = pygame
        self.screen = screen
        self.height = 100
        self.width = 40
        self.blocks_count = RESOLUTION[0] // self.width
        self.color = (0, 0, 0)
        self.x_surface = [i for i in range(0, RESOLUTION[0], self.width)]
        self.y_surface = [SURFACE_BOTTOM_BORDER + randint(-20, +20) for i in range(0, RESOLUTION[0], self.width)]

    def reveal(self):
        # rects = self.pygame.sprite.Group()
        for i in range(len(self.x_surface)):
            allowable_y = self.y_surface[i]
            allowable_x = self.x_surface[i]
            rect = (allowable_x, allowable_y, self.width, self.height)
            self.pygame.draw.rect(self.screen, self.color, rect)

    def generate(self):
        surface = []
        for i in range (0, RESOLUTION[0], 20):
            surface.append(i)

    def get_surface(self):
        return (self.x_surface, self.y_surface)