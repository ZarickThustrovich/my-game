import pygame  
import sys  
from pygame.locals import *


# initializing the constructor
game = pygame
game.init()
res = (720,720)  
screen = pygame.display.set_mode(res)  
width = screen.get_width()  
height = screen.get_height()  
running = True
is_menu = True

rect = pygame.Rect(30, 30, 60, 60)

class Snake:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.color = (222, 25, 22)
    
    def eat(self):
        return 0
    
    def draw(self):
        # return self.game.draw(self.screen, self.color, rect)
        pygame.draw(self.screen, self.color, rect)



def call_menu():
    global is_menu
    is_menu = True

def start_game():
    global is_menu
    is_menu = False


snake = Snake(game=game, screen=screen)


def menu(screen, game):
    # game.init()
    screen.fill((255, 0, 0))
    mouse = game.mouse.get_pos()
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                start_game()
        game.display.update()           

def gameplay(screen, game):
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    snake.draw()
    game.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            game.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                call_menu()
            
    screen.fill((255, 255, 255))
    for event in game.event.get():
        if event.type == game.QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                call_menu()
        game.display.update() 
    
    # game.display.flip()



while running:
    if is_menu:
        menu(screen, game)
    else:
        gameplay(screen, game)
        
game.quit()
sys.exit()
    
