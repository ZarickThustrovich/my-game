import pygame
import sys
from pygame.locals import *
from random import randint
import os.path



SPRITES_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sprites')


pygame.init()
res = (720, 720)
screen = pygame.display.set_mode(res)
running = True
is_menu = True
clock = pygame.time.Clock()


class Apple:
    def __init__(self, screen):
        self.screen = screen
        self.color = (222, 25, 22)
        self.x_coord = round(randint(20, res[0] - 20) / 20) * 20
        self.y_coord = round(randint(20, res[0] - 20) / 20) * 20
        self.exist = True
    
    def draw(self):
        rect = pygame.Rect(self.x_coord, self.y_coord, 20, 20)
        pygame.draw.rect(screen, self.color, rect)
    
    def get_coords(self):
        return self.x_coord, self.y_coord
    
    def remove(self):
        self.exist = False
    
    def is_exist(self):
        return self.exist
        

class SpriteSheet:
    def __init__(self, width:int, height:int, state:str, reversed:bool, accelerate:int, divider:int):
        self.width = width
        self.height = height
        self.state = state
        self.sheet = pygame.image.load(os.path.join(SPRITES_PATH, f"{state}.png")).convert_alpha()
        self.reversed = reversed
        self.accelerate = accelerate
        self.divider = divider
    
    def get_sprite(self):
        sprite = pygame.Surface([self.width, self.height], pygame.SRCALPHA)
        y = 0
        if self.reversed:
            reversed_by_divider = [i for i in range(0, self.divider)]
            reversed_x = reversed_by_divider[self.accelerate - 1]
            x = reversed_x * self.width
            sprite.blit(pygame.transform.flip(self.sheet, True, False), (0, 0), (x, y, self.width, self.height))
        else:
            x = self.accelerate * self.width
            sprite.blit(self.sheet, (0, 0), (x, y, self.width, self.height))
        print('x,y=', x, y)
        return sprite


class Player:
    def __init__(self, screen):
        global res
        self.screen = screen
        self.height = 64
        self.width = 100
        self.x = (res[0] - self.width) // 2
        self.y = res[1] - self.height - 20
        self.last_direction = 'idle'
        self.actions_counter = {'right': 0, 'left': 0, 'down': 0, 'idle': 0, 'jump': 0}
        self.falling = False
        self.image = SpriteSheet(self.width, self.height, 'idle_2', False, self.actions_counter['idle'], 4)
        print(os.path.join(SPRITES_PATH, "Idle_KG_1.png"))
    
    def set_last_direction(self, direction):
        self.last_direction = direction
    
    def idle(self, direction):
        reversed = direction == 'left'
        # print(f'idle: accelerate={self.accelerate_to["idle"]}')
        self.image = SpriteSheet(self.width, self.height, 'idle_1', False, self.actions_counter['idle'], 4)
        sprite = self.image.get_sprite()
        screen.blit(sprite, (self.x, self.y, self.width, self.height))
        pygame.display.flip()

    def idle_crouch(self):
        reversed = self.last_direction == 'left'
        # print(f'idle: accelerate={self.accelerate_to["idle"]}')
        self.image = SpriteSheet(self.width, self.height, 'crouching_idle', False, self.actions_counter['down'], 4)
        sprite = self.image.get_sprite()
        screen.blit(sprite, (self.x, self.y, self.width, self.height))
        pygame.display.flip()

    def idle_with_weapon(self):
        reversed = self.last_direction == 'left'
        self.image = SpriteSheet(self.width, self.height, 'idle_2', False, self.actions_counter['idle'], 4)
        sprite = self.image.get_sprite()
        screen.blit(sprite, (self.x, self.y, self.width, self.height))
        pygame.display.flip()
    
    def jump(self, direction):
        self.y -= 20
        if direction == 'left':
            self.x -= 10
        elif direction == 'right':
            self.x += 10
        self.falling = True
        reversed = self.last_direction == 'left'
        self.image = SpriteSheet(self.width, self.height, 'jump_1', reversed, self.actions_counter['jump'], 4)
        sprite = self.image.get_sprite()
        screen.blit(sprite, (self.x, self.y, self.width, self.height))
        pygame.display.flip()
    
    def set_is_falling(self, state):
        self.falling = state
    
    def check_collision_with_land(self):
        return self.y == res[1] - self.height - 20
        
    def check_if_landed(self):
        if self.check_collision_with_land():
            self.set_is_falling(False)
    
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
            if self.actions_counter['jump'] == 3:
                self.actions_counter['jump'] = 0
            else:
                self.actions_counter['jump'] += 1
                self.actions_counter['left'] = 0
                self.actions_counter['right'] = 0
                self.actions_counter['idle'] = 0
         
    def move(self):
        reversed = self.last_direction == 'left'
        self.image = SpriteSheet(self.width, self.height, 'walking_1', reversed, self.actions_counter[self.last_direction], 4)
        if self.last_direction == 'left':
            self.x -= 5
        elif self.last_direction == 'right':
            self.x += 5
        sprite = self.image.get_sprite()
        screen.blit(sprite, (self.x, self.y, self.width, self.height))
        pygame.display.flip()
    
    def move_crouch(self, direction):
        reversed = direction == 'left'
        self.image = SpriteSheet(self.width, self.height, 'crouching_walk_1', reversed, self.actions_counter[self.last_direction], 4)
        if self.last_direction == 'left':
            self.x -= 2
        elif self.last_direction == 'right':
            self.x += 2
        sprite = self.image.get_sprite()
        screen.blit(sprite, (self.x, self.y, self.width, self.height))
        pygame.display.flip()

            
player = Player(screen)


def call_menu():
    global is_menu
    is_menu = True

def start_game():
    global is_menu
    is_menu = False

def menu():
    screen.fill((255, 255, 255)) 
    pygame.display.update()
    
def gameplay():
    print(player.actions_counter)
    screen.fill((255, 255, 255))
    keys = pygame.key.get_pressed()
    if player.falling:
        player.check_if_landed()
        if player.falling:
            player.y += 2
            player.accelerate('jump')
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        if player.last_direction == 'right':
            player.accelerate('right')
            player.move_crouch('right')
        else:
            player.set_last_direction('right')
            player.idle('right')
        return 0
    elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        if player.last_direction == 'left':
            player.accelerate('left')
            player.move_crouch('left')
        else:
            player.set_last_direction('left')
            player.idle('left')
        return 0
    elif (keys[pygame.K_LEFT] and keys[pygame.K_UP]):
        if not player.falling:
            player.jump('left')
        else:
            player.accelerate('jump')
    elif (keys[pygame.K_RIGHT] and keys[pygame.K_UP]):
        if not player.falling:
            player.jump('right')
        else:
            player.accelerate('jump')
    elif keys[pygame.K_DOWN]:
        if player.last_direction == 'down':
            player.accelerate('down')
        else:
            player.set_last_direction('down')
        player.idle_crouch()
        return 0
    elif keys[pygame.K_RIGHT]:
        if player.last_direction == 'right':
            player.accelerate('right')
            player.move()
        else:
            player.set_last_direction('right')
            player.idle('right')
        return 0
    elif keys[pygame.K_LEFT]:
        if player.last_direction == 'left':
            player.accelerate('left')
            player.move()
        else:
            player.set_last_direction('left')
            player.idle('left')
        return 0
    elif keys[pygame.K_UP or pygame.K_SPACE]:
        if not player.falling:
            player.jump(None)
            return 0
    player.idle(player.last_direction)
    if player.last_direction == 'idle':
        player.accelerate('idle')
    else:
        player.set_last_direction(player.last_direction)
    pygame.display.update()

while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                if is_menu:
                    start_game()
                else:
                    call_menu()
    if is_menu:
        menu()
    else:
        gameplay()
    pygame.time.delay(10) 
    clock.tick(16)

pygame.quit()
sys.exit()
