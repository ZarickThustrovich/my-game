import pygame
import sys
from pygame.locals import *
from random import randint
import os.path
from player import Player
from in_game_menu import InGameMenu
from settings import (
    RESOLUTION,
    FRAMERATE,
    PLAYER_SPRITE_FRAMES,
    PLAYER_AIR_ACCELERATION,
    PLAYER_MOVING_SPEED,
    PLAYER_CROUCHING_SPEED,
    PLAYER_JUMP_HEIGHT,
    PLAYER_FALLING_SPEED,
    PLAYER_SPRINTING_SPEED,
)





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
    in_game_menu = InGameMenu(pygame, screen, player.health)
    screen.fill((255, 255, 255))
    print(player.x, ' ', player.y)
    keys = pygame.key.get_pressed()
    mouse_clicks = pygame.mouse.get_pressed()
    sprint = False
    in_game_menu.reveal()
    if player.stunned:
        player.damage(5)
        if player.health <= 0:
            return call_menu()
            
        pygame.display.update()
        return 0
    if keys[pygame.K_LCTRL]:
        player.damage(10)
        pygame.display.update()
        return 0
    if player.attacking:
        player.attack()
        pygame.display.update()
        return 0
    if mouse_clicks[0]:
        player.attack()
        pygame.display.update()
        return 0
    if keys[pygame.K_LSHIFT]:
        sprint = True
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
        player.move('right', sprint)
        return 0
    elif keys[pygame.K_LEFT]:
        player.move('left', sprint)
        return 0
    elif keys[pygame.K_UP or pygame.K_SPACE]:
        player.jump(None)
        return 0
    player.idle()
    pygame.display.update()

while running:
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
    clock.tick(FRAMERATE)

pygame.quit()
sys.exit()
