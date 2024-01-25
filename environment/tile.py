from spritesheet import Texture
from settings import ENVIRONMENT_SPRITES_FOLDER
import os


class Tile:
  def __init__(self, pygame, screen, size, coords, texture):
    self.width = size[0]
    self.height = size[1]
    self.texture = texture
    self.coords = coords
    self.pygame = pygame
    self.screen = screen
    self.image = None
    
  def reveal(self):
    self.image = self.get_texture()
    self.screen.blit(self.image, (self.coords, (self.width, self.height)))
    # self.pygame.display.flip()
  
  def get_texture(self):
    texture = Texture(
        self.width,
        self.height,
        os.path.join(ENVIRONMENT_SPRITES_FOLDER, self.texture + '.png'),
        self.pygame,
    )
    return texture.get()
    