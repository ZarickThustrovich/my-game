from spritesheet import SpriteSheet
from settings import (
    RESOLUTION, 
    PLAYER_SPRITE_FRAMES,
    PLAYER_JUMP_HEIGHT,
    PLAYER_AIR_ACCELERATION,
    PLAYER_CROUCHING_SPEED,
    PLAYER_MOVING_SPEED,
    PLAYER_FALLING_SPEED,
    PLAYER_SPRINTING_SPEED,
    SURFACE_BOTTOM_BORDER,
)


class Player:
    def __init__(self, screen, pygame):
        self.screen = screen
        self.height = 64
        self.width = 100
        self.x = (RESOLUTION[0] - self.width) // 2
        self.y = (SURFACE_BOTTOM_BORDER - self.height) - 20
        self.last_direction = 'idle'
        self.falling = False
        self.pygame = pygame
        self.animation_counter = 0
        self.state = 'idle'
        self.attacking = False
        self.image = self.get_spritesheet('idle_2')
     
    def get_spritesheet(self, state, player_sprite_frames=PLAYER_SPRITE_FRAMES):
        return SpriteSheet(
            self.width, 
            self.height, 
            state, 
            self.last_direction == 'left', 
            self.animation_counter, 
            player_sprite_frames, 
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
        self.image = self.get_spritesheet('crouching_idle_test')
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
        self.x = self.new_x(PLAYER_CROUCHING_SPEED)
        sprite = self.image.get_sprite()
        self.reveal(sprite, (self.x, self.y, self.width, self.height))

    def move(self, direction, sprint=False):
        self.set_last_direction(direction)
        if self.state != 'move':
            self.state = 'move'
        self.accelerate_animation()
        if self.falling:
            self.x = self.new_y(1)
        if not sprint:
            self.x = self.new_x(PLAYER_MOVING_SPEED)
            self.image = self.get_spritesheet('walking_1')
        else:
            self.x = self.new_x(PLAYER_SPRINTING_SPEED)
            self.image = self.get_spritesheet('walking_2')
        sprite = self.image.get_sprite()
        self.reveal(sprite, (self.x, self.y, self.width, self.height))
    
    def fall(self, direction=None):
        self.set_is_falling(True)
        if self.state != 'fall':
            self.set_last_direction(direction if direction else self.last_direction)
            self.state = 'fall'
        if self.is_landed():
            self.set_is_falling(False)
            self.image = self.get_spritesheet('idle_1')
            sprite = self.image.get_sprite()
            self.reveal(sprite, (self.x, self.y, self.width, self.height))
        else:
            if not direction:
                self.y = self.new_y(PLAYER_FALLING_SPEED)
            else:
                self.set_last_direction(direction)
                self.y = self.new_y(PLAYER_FALLING_SPEED)
                self.x = self.new_x(10, direction)
            self.image = self.get_spritesheet('jump_1')
            sprite = self.image.get_sprite()
            self.reveal(sprite, (self.x, self.y, self.width, self.height))
    
    def attack(self):
        self.attacking = True
        if self.animation_counter == 4:
            self.attacking = False
        if self.state != 'attack':
            self.stop_animation()
            self.state = 'attack'
        self.accelerate_animation()
        self.image = self.get_spritesheet('Attack_KG_4')
        sprite = self.image.get_sprite()
        self.reveal(sprite, (self.x, self.y, self.width, self.height)) 
    
    def jump(self, jump_direction=None):
        self.y = self.new_y(PLAYER_JUMP_HEIGHT)
        self.x = self.new_x(PLAYER_AIR_ACCELERATION, jump_direction)
        self.image = self.get_spritesheet('jump_1')
        sprite = self.image.get_sprite()
        self.falling = True
        self.reveal(sprite, (self.x, self.y, self.width, self.height))
        
    def new_x(self, speed:int, custom_direction=False):
        direction = custom_direction if custom_direction else self.last_direction
        return self.x - speed if direction == 'left' else self.x + speed
            
    def new_y(self, speed:int):
        return self.y + speed if self.falling else self.y - speed
        
    def set_is_falling(self, state):
        self.falling = state
    
    def check_collision_with_land(self):
        return self.y == SURFACE_BOTTOM_BORDER - self.height - 20
        
    def is_landed(self):
        return self.check_collision_with_land()

    def accelerate_animation(self):
        if self.animation_counter > 3:
            self.animation_counter = 0
        else:
            self.animation_counter += 1
    
    def stop_animation(self):
        self.animation_counter = 0
    
    def set_state(self, state:str):
        self.state = state