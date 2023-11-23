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
        

class Snake:
    def __init__(self, screen, game):
        self.screen = screen
        self.game = game
        self.x_coord = 0
        self.y_coord = 0
        self.color = (222, 25, 22)
        self.rects = [[self.x_coord, self.y_coord]]
        self.last_direction = 'right'

    def draw(self):
        new_rects = []
            # rect = pygame.Rect(self.x_coord, self.y_coord, 20, 20)
            # return pygame.draw.rect(self.screen, self.color, rect)
        if self.last_direction == 'down':
            new_rects = self.rects[:-1]
            new_rects.insert(0, [self.rects[0][0], self.rects[0][1] + 20])
        elif self.last_direction == 'up':
            new_rects = self.rects[:-1]
            new_rects.insert(0, [self.rects[0][0], self.rects[0][1] - 20])
        elif self.last_direction == 'left':
            new_rects = self.rects[:-1]
            new_rects.insert(0, [self.rects[0][0] - 20, self.rects[0][1]])
        elif self.last_direction == 'right':
            new_rects = self.rects[:-1]
            new_rects.insert(0, [self.rects[0][0] + 20, self.rects[0][1]])
        for rectangle in new_rects:
            rectangle_x, rectangle_y = rectangle
            rect = pygame.Rect(rectangle_x, rectangle_y, 20, 20)
            pygame.draw.rect(self.screen, self.color, rect)
        self.rects = new_rects
        self.x_coord = self.rects[0][0]
        self.y_coord = self.rects[0][1]
        if self.check_collision():
            global snake
            snake = Snake(game=pygame, screen=screen)
            call_menu()
        elif self.check_self_collision():
            call_menu()
            
    def set_last_direction(self, direction):
        if direction == 'up' and self.last_direction != 'down':
            self.last_direction = direction
        elif direction == 'down' and self.last_direction != 'up':
            self.last_direction = direction
        elif direction == 'right' and self.last_direction != 'left':
            self.last_direction = direction
        elif direction == 'left' and self.last_direction != 'right':
            self.last_direction = direction
    
    def make_longer(self):
        new_x_coord, new_y_coord = self.rects[len(self.rects) - 1]
        if self.last_direction == 'down':
            new_x_coord -= 20
        elif self.last_direction == 'up':
            new_y_coord += 20
        elif self.last_direction == 'left':
            new_x_coord += 20
        elif self.last_direction == 'right':
            new_x_coord -= 20
        
        self.x_coord = new_x_coord
        self.y_coord = new_y_coord
        self.rects.append([self.x_coord, self.y_coord])

    def check_self_collision(self):
        check_x, check_y = self.rects[0]
        print('check_x, check_y = ', check_x, check_y)
        print(self.rects)
        for body_part_x, body_part_y in self.rects[4:]:
            if (abs(check_x - body_part_x) <= 1 and abs(check_y - body_part_y) <= 1):
                return True
        return False
        
    def get_coords(self):
        return self.x_coord, self.y_coord

    def check_collision(self):
        if self.last_direction == 'down':
            if self.y_coord > 720:
                return True
        elif self.last_direction == 'up':
            if self.y_coord <= 0:
                return True
        elif self.last_direction == 'left':
            if self.x_coord <= 0:
                return True
        elif self.last_direction == 'right':
            if self.x_coord > 720:
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
    screen.fill((255, 255, 255)) 
    pygame.display.update()
    
def gameplay():
    global apple
    if not apple.is_exist():
        apple = Apple(screen=screen)
    screen.fill((255, 255, 255))    
    
    if event.type == KEYDOWN:
        if event.key == K_DOWN:
            snake.set_last_direction('down')
        elif event.key == K_UP:
            snake.set_last_direction('up')
        elif event.key == K_LEFT:
            snake.set_last_direction('left')
        elif event.key == K_RIGHT:
            snake.set_last_direction('right')
    
    snake.draw()
    apple.draw()
    
    apple_x, apple_y = apple.get_coords()
    snake_x, snake_y = snake.get_coords()
    
    if (abs(snake_x - apple_x) <= 1 and abs(apple_y - snake_y) <= 1):
        apple.remove()
        snake.make_longer()
        
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
