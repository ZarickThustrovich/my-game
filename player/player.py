from spritesheet import SpriteSheet
from settings import RESOLUTION


class Player:
    def __init__(self, screen, pygame):
        self.screen = screen
        self.height = 64
        self.width = 100
        self.x = (RESOLUTION[0] - self.width) // 2
        self.y = (RESOLUTION[1] - self.height) - 20
        self.last_direction = 'idle'
        self.actions_counter = {'right': 0, 'left': 0, 'down': 0, 'idle': 0, 'jump': 0}
        self.falling = False
        self.pygame = pygame
        self.image = self.get_spritesheet('idle_2', 'idle')
     
    def get_spritesheet(self, state, actions_counter_key):
        return SpriteSheet(self.width, self.height, state, self.last_direction == 'left', self.actions_counter[actions_counter_key], 4, self.pygame)
    
    def set_last_direction(self, direction):
        self.last_direction = direction
    
    def idle(self):
        self.image = self.get_spritesheet('idle_1', 'idle')
        sprite = self.image.get_sprite()
        self.screen.blit(sprite, (self.x, self.y, self.width, self.height))
        self.pygame.display.flip()

    def idle_crouch(self):
        self.image = self.get_spritesheet('crouching_idle', 'down')
        sprite = self.image.get_sprite()
        self.screen.blit(sprite, (self.x, self.y, self.width, self.height))
        self.pygame.display.flip()

    def idle_with_weapon(self):
        self.image = self.get_spritesheet('idle_2', 'idle')
        sprite = self.image.get_sprite()
        self.screen.blit(sprite, (self.x, self.y, self.width, self.height))
        self.pygame.display.flip()
    
    def jump(self, direction):
        self.y -= 40
        if direction == 'left':
            self.x -= 10
        elif direction == 'right':
            self.x += 10
        self.falling = True
        self.image = self.get_spritesheet('jump_1', 'jump')
        sprite = self.image.get_sprite()
        self.screen.blit(sprite, (self.x, self.y, self.width, self.height))
        self.pygame.display.flip()
    
    def set_is_falling(self, state):
        self.falling = state
    
    def check_collision_with_land(self):
        return self.y == RESOLUTION[1] - self.height - 20
        
    def check_if_landed(self):
        if self.check_collision_with_land():
            self.set_is_falling(False)
            self.accelerate('jump', disable=True)
    
    def accelerate(self, action, disable=False):
        if action == 'idle':
            if self.actions_counter['idle'] == 3:
                self.actions_counter['idle'] = 0
            else:
                self.actions_counter['idle'] += 1
            self.actions_counter['right'] = 0
            self.actions_counter['left'] = 0
            self.actions_counter['down'] = 0
        elif action == 'left':
            if self.actions_counter['left'] == 4:
                self.actions_counter['left'] = 0
            else:
                self.actions_counter['left'] += 1
            self.actions_counter['right'] = 0
            self.actions_counter['idle'] = 0
            self.actions_counter['down'] = 0
        elif action == 'right':
            if self.actions_counter['right'] == 4:
                self.actions_counter['right'] = 0
            else:
                self.actions_counter['right'] += 1
            self.actions_counter['left'] = 0
            self.actions_counter['idle'] = 0
            self.actions_counter['down'] = 0
        elif action == 'down':
            if self.actions_counter['down'] == 2:
                self.actions_counter['down'] = 0
            else:
                self.actions_counter['down'] += 1
            self.actions_counter['left'] = 0
            self.actions_counter['idle'] = 0
            self.actions_counter['right'] = 0
        elif action == 'jump':
            if disable:
                self.actions_counter['jump'] = 0
                return 0
            if self.actions_counter['jump'] == 6:
                self.actions_counter['jump'] = 0
            else:
                self.actions_counter['jump'] += 1
                self.actions_counter['left'] = 0
                self.actions_counter['right'] = 0
                self.actions_counter['idle'] = 0
         
    def move(self):
        if self.falling:
            if self.last_direction == 'left':
                self.x -= 5
                return 0
            elif self.last_direction == 'right':
                self.x += 5
                return 0
        self.image = self.get_spritesheet('walking_1', self.last_direction)
        if self.last_direction == 'left':
            self.x -= 5
        elif self.last_direction == 'right':
            self.x += 5
        sprite = self.image.get_sprite()
        self.screen.blit(sprite, (self.x, self.y, self.width, self.height))
        self.pygame.display.flip()
    
    def move_crouch(self, direction):
        self.image = self.get_spritesheet('crouching_walk_1', direction)
        if self.last_direction == 'left':
            self.x -= 2
        elif self.last_direction == 'right':
            self.x += 2
        sprite = self.image.get_sprite()
        self.screen.blit(sprite, (self.x, self.y, self.width, self.height))
        self.pygame.display.flip()