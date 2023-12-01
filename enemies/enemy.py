from spritesheet import SpriteSheet
from settings import (
    ENEMY_SPRITES_FOLDER,
    ENEMY_HEALTH,
    ENEMY_MOVING_SPEED,
    ENEMY_SPRITE_FRAMES,
)
import os


class Enemy:
    def __init__(self, screen, pygame, genus, x, y):
        self.pygame = pygame
        self.screen = screen
        self.x = x
        self.y = y
        self.width = 287.5
        self.height = 180
        self.genus = genus
        self.health = ENEMY_HEALTH
        self.last_direction = 'left'
        self.animation_counter = 0
        self.state = 'move'
        self.falling = False
        
    def move(self, direction):
        self.set_last_direction(direction)
        if self.state != 'move':
            self.state = 'move'
        self.accelerate_animation()
        if self.falling:
            self.x = self.new_y(1)
        # self.x = self.new_x(ENEMY_MOVING_SPEED)
        self.image = self.get_spritesheet('demon_walk')
        sprite = self.image.get_sprite()
        self.reveal(sprite, (self.x, self.y, self.width, self.height))

    def accelerate_animation(self):
        if self.animation_counter > 3:
            self.animation_counter = 0
        else:
            self.animation_counter += 1

    def set_last_direction(self, direction):
        self.last_direction = direction
    
    def reveal(self, sprite, coords_and_sizes):
        self.screen.blit(sprite, coords_and_sizes)
        # self.pygame.display.flip()
        
    def new_x(self, speed:int, custom_direction=False):
        direction = custom_direction if custom_direction else self.last_direction
        return self.x - speed if direction == 'left' else self.x + speed
            
    def new_y(self, speed:int):
        return self.y + speed if self.falling else self.y - speed  

     
    def get_spritesheet(self, state, player_sprite_frames=ENEMY_SPRITE_FRAMES):
        return SpriteSheet(
            self.width, 
            self.height, 
            os.path.join(ENEMY_SPRITES_FOLDER, state + '.png'), 
            self.last_direction == 'left', 
            self.animation_counter, 
            player_sprite_frames, 
            self.pygame
        )