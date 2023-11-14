import pygame  
import sys  
from pygame.locals import *



    


# initializing the constructor
game = pygame
game.init()
# pygame.init()  
  
# screen resolution  
res = (720,720)  
  
# opens up a window  
screen = pygame.display.set_mode(res)  
  
# white color  
color = (255,255,255)  
  
# light shade of the button  
color_light = (170,170,170)  
  
# dark shade of the button  
color_dark = (100,100,100)  
  
# stores the width of the  
# screen into a variable  
width = screen.get_width()  
  
# stores the height of the  
# screen into a variable  
height = screen.get_height()  

# defining a font  
smallfont = pygame.font.SysFont('Corbel',35)  
  
# rendering a text written in  
# this font  


is_menu = False

def call_menu():
    is_menu = True


def menu(screen, game):
    start_text = smallfont.render('start', True, color)
    menu_text = smallfont.render('menu', True, color)
    quit_text = smallfont.render('quit' , True , color)
    for ev in pygame.event.get():  
        if ev.type == pygame.QUIT:  
            pygame.quit()  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    call_menu()

        # Fill the background with white
        screen.fill((255, 255, 255))

        # Draw a solid blue circle in the center
        pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

        # Flip the display
        pygame.display.flip()
              
        pygame.quit()  
        # fills the screen with a color  
        screen.fill((60,25,60))
          
        # stores the (x,y) coordinates into  
        # the variable as a tuple  
        mouse = pygame.mouse.get_pos()
          
        # if mouse is hovered on a button it  
        # changes to lighter shade  

          
        # updates the frames of the game  
        pygame.display.update()  
    
    if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:  
        game.draw.rect(screen,color_light,[width/2,height/2,140,40])          
    else:  
        game.draw.rect(screen,color_dark,[width/2,height/2,140,40])  
    
    if width/2 <= mouse[0] <= width/2+140 and height/2.5 <= mouse[1] <= height/2.5+40:  
        game.draw.rect(screen,color_light,[width/2,height/2.5,140,40])
          
    else:  
        game.draw.rect(screen,color_dark,[width/2,height/2.5,140,40])
        
    # superimposing the text onto our button
    screen.blit(start_text, (width/2+60,height/2.5)) 
    screen.blit(quit_text , (width/2+50,height/2))

def gameplay(screen, game):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                is_menu = True
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.display.flip()



while True:
    if is_menu:
        menu(screen, game)
    else:
        gameplay(screen, game)

while True:  
      
    for ev in pygame.event.get():  
          
        if ev.type == pygame.QUIT:  
            pygame.quit()  
              
        #checks if a mouse is clicked
        if ev.type == pygame.MOUSEBUTTONDOWN:  
              
            #if the mouse is clicked on the
            # button the game is terminated
            if width/2 <= mouse[0] <= width/2+140 and height/2.5 <= mouse[1] <= height/2+60:
                while running:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                        elif event.type == KEYDOWN:
                            if event.key == K_ESCAPE:
                                menu(screen)
                                running = False

                    # Fill the background with white
                    screen.fill((255, 255, 255))

                    # Draw a solid blue circle in the center
                    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)

                    # Flip the display
                    pygame.display.flip()
              
            if width/2 <= mouse[0] <= width/2+140 and height/2 <= mouse[1] <= height/2+40:  
                pygame.quit()  
                  
    # fills the screen with a color  
    screen.fill((60,25,60))
      
    # stores the (x,y) coordinates into  
    # the variable as a tuple  
    mouse = pygame.mouse.get_pos()
      
    # if mouse is hovered on a button it  
    # changes to lighter shade  

      
    # updates the frames of the game  
    pygame.display.update()  
pygame.quit()
