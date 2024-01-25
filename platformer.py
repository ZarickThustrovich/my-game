import pygame
import sys
from pygame.locals import *
from player import Player
from enemies import Enemy
from environment import Surface
from menu import Menu
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
screen_offset_x = max(0, 40 - RESOLUTION[0] // 2)
screen = pygame.display.set_mode((RESOLUTION[0] + screen_offset_x, RESOLUTION[1]))
# screen = pygame.Surface(RESOLUTION)
# screen_base.blit(screen, (0, 0))
# pygame.display.flip()
running = True
is_menu = True

def call_menu():
    global is_menu
    is_menu = True

def start_game():
    global is_menu
    is_menu = False

clock = pygame.time.Clock()
surface = Surface(pygame, screen)
surface.load_level('level-1')
surface.reveal()

player = Player(screen, pygame, call_menu, surface)
# enemy = Enemy(screen, pygame, 'knight', 0, 0)
menu = Menu(pygame, screen)
    
def gameplay():
    # print(enemy.x, ' ', enemy.y)
    global player
    if player.reset:
        player = Player(screen, pygame, call_menu, surface)
    # in_game_menu = InGameMenu(pygame, screen, player.health)
    screen.fill((255, 255, 255))
    # enemy.move('left')
    # print(player.x, ' ', player.y)
    keys = pygame.key.get_pressed()
    mouse_clicks = pygame.mouse.get_pressed()
    sprint = False
    # in_game_menu.reveal()
    surface.reveal()
    
    if player.stunned:
        player.damage(5)
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
        menu.reveal()
        menu.reveal_buttons()
    else:
        gameplay()
    pygame.time.delay(10)
    clock.tick(FRAMERATE)

pygame.quit()
sys.exit()
