import pygame
import sys
from pygame.locals import *
from random import randint
import os.path
from player import Player


SPRITES_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'sprites')


pygame.init()
res = (720, 720)
screen = pygame.display.set_mode(res)
running = True
is_menu = True
clock = pygame.time.Clock()
player = Player(screen, pygame)


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
            pygame.display.update()
            player.y += 2
            player.accelerate('jump')
            pygame.display.update()
            player.y += 2
            player.accelerate('jump')
            pygame.display.update()
            player.y += 2
            player.accelerate('jump')
            pygame.display.update()
            if keys[pygame.K_RIGHT]:
                player.move()
                player.set_last_direction('right')
                pygame.display.update()
                return 0
            elif keys[pygame.K_LEFT]:
                player.move()
                player.set_last_direction('left')
                player.accelerate('jump')
                pygame.display.update()
                return 0    
            player.accelerate('jump')
            pygame.display.update()
            return 0
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        if player.last_direction == 'right':
            player.accelerate('right')
            player.move_crouch('right')
        else:
            player.set_last_direction('right')
            player.idle()
        return 0
    elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        if player.last_direction == 'left':
            player.accelerate('left')
            player.move_crouch('left')
        else:
            player.set_last_direction('left')
            player.idle()
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
    elif keys[pygame.K_UP or pygame.K_SPACE]:
        if not player.falling:
            player.jump(None)
            return 0
    player.idle()
    if player.actions_counter['idle'] > 0:
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
