import pygame
import sys
from pygame.locals import *
from random import randint


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
        

class Player:
    def __init__(self, screen, game):
        self.screen = screen
        self.image = pygame.image.load("sprites/Idle_KG_1.png").convert_alpha()
    
        

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
    player = Player(screen)
    global apple
    if not apple.is_exist():
        apple = Apple(screen=screen)
    screen.fill((255, 255, 255))    
    
    if event.type == KEYDOWN:
        if event.key == K_DOWN:
            return 0
            # snake.set_last_direction('down')
        elif event.key == K_UP:
            return 0
            # snake.set_last_direction('up')
        elif event.key == K_LEFT:
            return 0
            # snake.set_last_direction('left')
        elif event.key == K_RIGHT:
            return 0
            # snake.set_last_direction('right')
    
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
    clock.tick(16)

pygame.quit()
sys.exit()
