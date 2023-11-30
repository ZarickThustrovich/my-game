from spritesheet import SpriteSheet
from settings import (
    RESOLUTION, 
    PLAYER_SPRITE_FRAMES,
)


class Player:
    def __init__(self, screen, pygame):
        self.screen = screen
        self.height = 64
        self.width = 100
        self.x = (RESOLUTION[0] - self.width) // 2
        self.y = (RESOLUTION[1] - self.height) - 20
        self.last_direction = 'idle'
        self.falling = False
        self.pygame = pygame
        self.animation_counter = 0
        self.state = 'idle'
        self.image = self.get_spritesheet('idle_2')
     
    def get_spritesheet(self, state):
        return SpriteSheet(
            self.width, 
            self.height, 
            state, 
            self.last_direction == 'left', 
            self.animation_counter, 
            PLAYER_SPRITE_FRAMES, 
            self.pygame
        )
    
    def set_last_direction(self, direction):
        self.last_direction = direction
    
    def reveal(self, sprite, coords_and_sizes):
        self.screen.blit(sprite, coords_and_sizes)
        self.pygame.display.flip()
        
    def idle(self):
        if self.state != 'idle':
            self.stop_animation()
            self.state = 'idle'
        self.accelerate_animation()
        self.image = self.get_spritesheet('idle_1')
        sprite = self.image.get_sprite()
        self.reveal(sprite, (self.x, self.y, self.width, self.height))

    def idle_crouch(self):
        if self.state != 'crouching_idle':
            self.stop_animation()
            self.state = 'crouching_idle'
        self.accelerate_animation()
        self.image = self.get_spritesheet('crouching_idle')
        sprite = self.image.get_sprite()
        self.reveal(sprite, (self.x, self.y, self.width, self.height))

    def idle_with_weapon(self):
        if self.state != 'idle_with_weapon':
            self.state = 'idle_with'
        self.stop_animation()
        self.state = 'idle_with_weapon'
        self.accelerate_animation()
        self.image = self.get_spritesheet('idle_2')
        sprite = self.image.get_sprite()
        self.reveal(sprite, (self.x, self.y, self.width, self.height))

    def move_crouch(self, direction):
        self.set_last_direction(direction)
        if self.state != 'crouching_walk':
            self.state = 'crouching_walk'
            self.stop_animation()
        self.state = 'crouching_walk'
        self.accelerate_animation()
        self.image = self.get_spritesheet('crouching_walk_1')
        self.last_direction = direction
        self.x = self.new_x(2)
        sprite = self.image.get_sprite()
        self.reveal(sprite, (self.x, self.y, self.width, self.height))

    def move(self, direction):
        if self.state != 'move':
            self.set_last_direction(direction)
            self.state = 'move'
        self.accelerate_animation()
        if self.falling:
            self.x = self.new_y(1)
        self.image = self.get_spritesheet('walking_1')
        self.x = self.new_x(5)
        sprite = self.image.get_sprite()
        self.reveal(sprite, (self.x, self.y, self.width, self.height))
    
    def fall(self, direction=None):
        if self.state != 'fall':
            self.set_last_direction(direction if direction else self.last_direction)
            self.state = 'fall'
        sprite = self.image.get_sprite()
        self.reveal(sprite, (self.x, self.y, self.width, self.height))
        if self.is_landed():
            self.falling = False
        if not self.falling:
            self.image = self.get_spritesheet('idle_1')
            sprite = self.image.get_sprite()
            self.reveal(sprite, (self.x, self.y, self.width, self.height))
        else:
            if not direction:
                self.y = self.new_y(40)
            else:
                self.y = self.new_y(10)
                self.x = self.new_x(10, direction)
            self.image = self.get_spritesheet('jump_1')
            sprite = self.image.get_sprite()
            self.reveal(sprite, (self.x, self.y, self.width, self.height))
            
    
    def jump(self, jump_direction=None):
        if self.is_landed():
            self.falling = False
            self.y = self.new_y(40)
            self.x = self.new_x(10, jump_direction)
        else:
            self.falling = True
        self.image = self.get_spritesheet('jump_1')
        sprite = self.image.get_sprite()
        self.reveal(sprite, (self.x, self.y, self.width, self.height))
        
    def new_x(self, speed:int, custom_direction=False):
        direction = custom_direction if custom_direction else self.last_direction
        return self.x - speed if direction == 'left' else self.x + speed
            
    def new_y(self, speed:int):
        return self.y + speed if self.falling else self.y - speed
        
    def set_is_falling(self, state):
        self.falling = state
    
    def check_collision_with_land(self):
        return self.y == RESOLUTION[1] - self.height - 20
        
    def is_landed(self):
        if self.check_collision_with_land():
            self.set_is_falling(False)
    
    def accelerate_animation(self):
        if self.animation_counter > 3:
            self.animation_counter = 0
        else:
            self.animation_counter += 1
    
    def stop_animation(self):
        self.animation_counter = 0
    
    def set_state(self, state:str):
        self.state = state