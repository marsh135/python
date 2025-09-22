import pygame
pygame.init()
class Player:
    def __init__(self, x, y, w, h, speed, r, g, b):
        self.x = x
        self.y = y
        self. w = w
        self.h = h
        self.r =  r
        self.g = g
        self.b = b
        self.speed =  speed
    
    def move(self, dx, dy):
        self.x += dx * self.speed
        self.y += dy * self.speed
    
    def draw(self, screen):
        pygame.draw.circle(screen, (self.r,self.g,self.b), (self.x, self.y), self.w)


width = 800
height = 600

screen = pygame.display.set_mode((width, height))

player1 =  Player(250, 250, 100,100, 1, 255, 0,0)

player2 =  Player(100, 100, 50, 50, 2, 0,255,0)
player3 =  Player(500, 500, 33, 33, 6, 0,0, 122)
running =  True
while running:

    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running =  False
        elif event.type ==  pygame.KEYDOWN:
            if event.key == pygame.K_q:
                running = False
    
    keys =  pygame.key.get_pressed()
    
    dx=0
    dy=0
    if keys[pygame.K_LEFT]:
        dx-=1
    if keys[pygame.K_RIGHT]:
        dx+=1
    if keys[pygame.K_UP]:
        dy-=1
    if keys[pygame.K_DOWN]:
        dy+=1

    dx2=0
    dy2=0
    if keys[pygame.K_a]:
        dx2-=1
    if keys[pygame.K_d]:
        dx2+=1
    if keys[pygame.K_w]:
        dy2-=1
    if keys[pygame.K_s]:
        dy2+=1
#move that second object using WASD
        
    
    player1.move(dx, dy)
    player2.move(dx2, dy2)
    player3.draw(screen)

    player1.draw(screen)
    player2.draw(screen)

    pygame.display.flip()

pygame.quit()

