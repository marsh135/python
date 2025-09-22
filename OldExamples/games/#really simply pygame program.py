#really simply pygame program

import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
r = 255
g = 255
b = 255

screen = pygame.display.set_mode([500,500])

#run until the user asks to quit
running =  True

while running:
    #did the user press the close button?
     #if so, close app,and terminate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #fill the background
    screen.fill((r,g,b))

    #draw a shape
    pygame.draw.circle(screen, (255,0,0), (250,250), 50)

    pygame.display.flip()
    
pygame.quit()