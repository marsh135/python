#really simply pygame program
import pygame
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
r = 200
g = 135
b = 42
#base the screen size on variables
screen = pygame.display.set_mode([SCREEN_WIDTH,SCREEN_HEIGHT])

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
    #base center on variables
    
    pygame.draw.circle(screen, (42,135,200), (SCREEN_WIDTH/2,SCREEN_HEIGHT*.5), 50)
    
    pygame.draw.rect(screen, (100,100,100), (400, 300, 100, 50))

    

    pygame.display.flip()
    
pygame.quit()