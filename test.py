import pygame
import sys
from pygame.locals import *
from random import randint


pygame.init()
res = (720, 720)
screen = pygame.display.set_mode(res)
running = True
is_menu = True


class Apple:
    def __init__(self, screen):
        self.screen = screen
        self.color = (222, 25, 22)
        self.x_coord = randint(20, res[0] - 20)
        self.y_coord = randint(20, res[0] - 20)
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
        

class Snake:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.x_coord = 10
        self.y_coord = 10
        self.color = (222, 25, 22)
        self.rects = [[self.x_coord, self.y_coord]]
        self.last_direction = None

    def draw(self):
        new_rects = []
        if self.last_direction == None:
            new_rects = self.rects
            for rectangle in new_rects:
                rectangle_x, rectangle_y = rectangle
                rect = pygame.Rect(rectangle_x, rectangle_y, 20, 20)
                pygame.draw.rect(self.screen, self.color, rect)
            return 0
        print('fucntion started ', self.rects)
        if self.check_collision():
            rect = pygame.Rect(self.x_coord, self.y_coord, 20, 20)
            return pygame.draw.rect(self.screen, self.color, rect)
        if self.last_direction == 'down':
            for rect_x, rect_y in self.rects:
                new_rects.append([rect_x, rect_y + 20])
        elif self.last_direction == 'up':
            for rect_x, rect_y in self.rects:
                new_rects.append([rect_x, rect_y - 20])
        elif self.last_direction == 'left':
            for rect_x, rect_y in self.rects:
                new_rects.append([rect_x - 20, rect_y])
        elif self.last_direction == 'right':
            for rect_x, rect_y in self.rects:
                new_rects.append([rect_x + 20, rect_y])
        else:
            new_rects = self.rects
        for rectangle in new_rects:
            rectangle_x, rectangle_y = rectangle
            rect = pygame.Rect(rectangle_x, rectangle_y, 20, 20)
            pygame.draw.rect(self.screen, self.color, rect)
        self.rects = new_rects
        self.x_coord = self.rects[0][0]
        self.y_coord = self.rects[0][1]
        print('fucntion ended ', self.rects)
    
    def set_last_direction(self, direction):
        self.last_direction = direction
    
    def make_longer(self):
        new_x_coord = self.x_coord
        new_y_coord = self.y_coord
        
        if self.last_direction == 'down':
            new_x_coord = self.x_coord + 20
        elif self.last_direction == 'up':
            new_y_coord = self.y_coord - 20
        elif self.last_direction == 'left':
            new_x_coord = self.x_coord - 20
        elif self.last_direction == 'right':
            new_x_coord = self.x_coord + 20
        
        self.x_coord = new_x_coord
        self.y_coord = new_y_coord
        self.rects.append([new_x_coord, new_y_coord])

        
    
    def get_coords(self):
        return self.x_coord, self.y_coord

    def check_collision(self):
        if self.last_direction == 'down':
            if self.y_coord >= 690:
                return True
        elif self.last_direction == 'up':
            if self.y_coord <= 20:
                return True
        elif self.last_direction == 'left':
            if self.x_coord < 20:
                return True
        elif self.last_direction == 'right':
            if self.x_coord > 680:
                return True
        else:
            return False
        return False
            
snake = Snake(game=pygame, screen=screen)
apple = Apple(screen=screen)

def call_menu():
    global is_menu
    is_menu = True

def start_game():
    global is_menu
    is_menu = False

def menu():
    screen.fill((255, 0, 0))
    pygame.display.update()

def gameplay():
    global apple
    if not apple.is_exist():
        apple = Apple(screen=screen)
    screen.fill((255, 255, 255))    
    
    if event.type == KEYDOWN:
        if event.key == K_DOWN:
            # snake.move('down')
            snake.set_last_direction('down')
        elif event.key == K_UP:
            # snake.move('up')
            snake.set_last_direction('up')
        elif event.key == K_LEFT:
            # snake.move('left')
            snake.set_last_direction('left')
        elif event.key == K_RIGHT:
            # snake.move('right')
            snake.set_last_direction('right')
    else:
        snake.set_last_direction(None)
    
    snake.draw()
    apple.draw()
    
    apple_x, apple_y = apple.get_coords()
    snake_x, snake_y = snake.get_coords()
    
    if (abs(snake_x - apple_x) <= 30 and abs(apple_y - snake_y) <= 30):
        apple.remove()
        snake.make_longer()
        
    # Update the display
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

    pygame.time.delay(10)  # Added a small delay to reduce CPU usage

pygame.quit()
sys.exit()
