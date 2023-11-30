import pygame
import sys
from pygame.locals import *
from random import randint
import os.path
from player import Player
from settings import RESOLUTION





pygame.init()
screen = pygame.display.set_mode(RESOLUTION)
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
    print(player.x, ' ', player.y)
    # print(player.actions_counter)
    screen.fill((255, 255, 255))
    keys = pygame.key.get_pressed()
    if player.falling:
        if keys[pygame.K_RIGHT]:
            player.fall('right')
        elif keys[pygame.K_LEFT]:
            player.fall('left')
        else:
            player.fall()
        pygame.display.update()
        return 0
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        player.move_crouch('right')
        return 0
    elif keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        player.move_crouch('left')
        return 0
    elif (keys[pygame.K_LEFT] and keys[pygame.K_UP]):
        if not player.falling:
            player.jump('left')
            return 0
    elif (keys[pygame.K_RIGHT] and keys[pygame.K_UP]):
        if not player.falling:
            player.jump('right')
            return 0
    elif keys[pygame.K_DOWN]:
        player.idle_crouch()
        return 0
    elif keys[pygame.K_RIGHT]:
        player.move('right')
        return 0
    elif keys[pygame.K_LEFT]:
        player.move('left')
        return 0
    elif keys[pygame.K_UP or pygame.K_SPACE]:
        if not player.falling:
            player.jump(None)
            return 0
    player.idle()
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
