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
            reversed_by_divider = [i for i in range(1, self.divider + 1)]
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
        self.accelerate_to = {'right': 0, 'left': 0, 'down': 0, 'idle': 0}
        self.image = SpriteSheet(self.width, self.height, 'idle_2', False, self.accelerate_to['idle'], 4)
        print(os.path.join(SPRITES_PATH, "Idle_KG_1.png"))
    
    def set_last_direction(self, direction):
        self.last_direction = direction
    
    def idle(self):
        reversed = self.last_direction == 'left'
        # print(f'idle: accelerate={self.accelerate_to["idle"]}')
        self.image = SpriteSheet(self.width, self.height, 'idle_1', False, self.accelerate_to['idle'], 4)
        sprite = self.image.get_sprite()
        screen.blit(sprite, (self.x, self.y, self.width, self.height))
        pygame.display.flip()

    def idle_crouch(self):
        reversed = self.last_direction == 'left'
        # print(f'idle: accelerate={self.accelerate_to["idle"]}')
        self.image = SpriteSheet(self.width, self.height, 'crouching_idle', False, self.accelerate_to['down'], 4)
        sprite = self.image.get_sprite()
        screen.blit(sprite, (self.x, self.y, self.width, self.height))
        pygame.display.flip()

    def idle_with_weapon(self):
        reversed = self.last_direction == 'left'
        self.image = SpriteSheet(self.width, self.height, 'idle_2', False, self.accelerate_to['idle'], 4)
        sprite = self.image.get_sprite()
        screen.blit(sprite, (self.x, self.y, self.width, self.height))
        pygame.display.flip()
    
    def accelerate(self, direction):
        if direction == 'idle':
            if self.accelerate_to['idle'] == 3:
                self.accelerate_to['idle'] = 0
            else:
                self.accelerate_to['idle'] += 1
            self.accelerate_to['right'] = 0
            self.accelerate_to['left'] = 0
            self.accelerate_to['down'] = 0
        elif direction == 'left':
            if self.accelerate_to['left'] == 3:
                self.accelerate_to['left'] = 0
            else:
                self.accelerate_to['left'] += 1
            self.accelerate_to['right'] = 0
            self.accelerate_to['idle'] = 0
            self.accelerate_to['down'] = 0
        elif direction == 'right':
            if self.accelerate_to['right'] == 3:
                self.accelerate_to['right'] = 0
            else:
                self.accelerate_to['right'] += 1
            self.accelerate_to['left'] = 0
            self.accelerate_to['idle'] = 0
            self.accelerate_to['down'] = 0
        elif direction == 'down':
            if self.accelerate_to['down'] == 3:
                self.accelerate_to['down'] = 0
            else:
                self.accelerate_to['down'] += 1
            self.accelerate_to['left'] = 0
            self.accelerate_to['idle'] = 0
            self.accelerate_to['right'] = 0
    def move(self):
        reversed = self.last_direction == 'left'
        self.image = SpriteSheet(self.width, self.height, 'walking_1', reversed, self.accelerate_to[self.last_direction], 4)
        if self.last_direction == 'left':
            self.x -= 5
        elif self.last_direction == 'right':
            self.x += 5
        sprite = self.image.get_sprite()
        screen.blit(sprite, (self.x, self.y, self.width, self.height))
        pygame.display.flip()
    
    def move_crouch(self, direction):
        reversed = direction == 'left'
        self.image = SpriteSheet(self.width, self.height, 'crouching_walk_1', reversed, self.accelerate_to[self.last_direction], 4)
        if self.last_direction == 'left':
            self.x -= 5
        elif self.last_direction == 'right':
            self.x += 5
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
    print(player.accelerate_to)
    screen.fill((255, 255, 255))    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        if player.last_direction == 'right':
            player.accelerate('right')
            player.move_crouch('right')
        else:
            player.set_last_direction('right')
            player.idle()
        print('player crouch forward')
        return 0
    elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        if player.last_direction == 'left':
            player.accelerate('left')
            player.move_crouch('left')
        else:
            player.set_last_direction('left')
            player.idle()
        print('player crouch backward')
        return 0
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
            player.idle()
        return 0
    elif keys[pygame.K_LEFT]:
        if player.last_direction == 'left':
            player.accelerate('left')
            player.move()
        else:
            player.set_last_direction('left')
            player.idle()
        return 0
    player.idle()
    if player.last_direction == 'idle':
        player.accelerate('idle')
    else:
        player.set_last_direction('idle')
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
