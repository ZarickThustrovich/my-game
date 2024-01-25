from settings import (
    RESOLUTION,
    SURFACE_BOTTOM_BORDER,
    TILE_DEFAULT_SIZE,
)
from .tile import Tile
import json

#Сделать логику генерации уровня из файла конфига level-1.json, с использованием класса Tile


class Surface:
    def __init__(self, pygame, screen):
        self.level_surface_data = []
        self.pygame = pygame
        self.screen = screen
        self.color = (0, 0, 0)

    def reveal(self):
        for i, tile_data in enumerate(self.level_surface_data['tiles'], 0):
            tile = Tile(
                self.pygame,
                self.screen,
                TILE_DEFAULT_SIZE,
                (
                    i * TILE_DEFAULT_SIZE[0],
                    tile_data['y_position'],
                ),
                tile_data['texture'],
            )
            tile.reveal()
            for y in range(1, (RESOLUTION[0] // TILE_DEFAULT_SIZE[1])):
                tile = Tile(
                    self.pygame,
                    self.screen,
                    TILE_DEFAULT_SIZE,
                    (
                        i * TILE_DEFAULT_SIZE[0],
                        (y * TILE_DEFAULT_SIZE[0]) + tile_data['y_position'],
                    ),
                    'ground-under',
                )
                tile.reveal()

    def get_surface(self):
        return self.level_surface_data
    
    def get_level_file_path(self, filename):
        import os
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), f'levels/{filename}')
    
    def load_level(self, filename):
        file_path = self.get_level_file_path(filename + '.json')
        with open(file_path) as file:
            self.level_surface_data = json.load(file)