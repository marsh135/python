import pygame
pygame.init()

class Player:
    def __init__(that, x, y, width, height, speed, colorR, colorG, colorB):
        that.x = x
        that.y =  y
        that.width = width
        that.height = height
        that.speed =  speed
        that.colorR = colorR
        that.colorG = colorG
        that.colorB = colorB
    
    def move(that, dx, dy):
        that.x += dx * that.speed
        that.y += dy * that.speed

    def draw(that, screen):
        pygame.draw.rect(screen, (that.colorR, that.colorG, that.colorB), pygame.Rect(that.x, that.y,that.width, that.height ))


width = 800
height = 600

screen = pygame.display.set_mode((width, height))


#tuples for shapes

rectangle_position = (350, 250)
rectangle_size = (100,100)

player =  Player(350, 250, 100, 100, 1, 255, 0,0)

player2 =  Player( 150, 200, 50, 50, 3, 0,255,0)
player3 = Player(600, 500, 25,100, 1, 0,0,255)

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
    p1dx = 0
    p1dy = 0


    p2dx = 0
    p2dy = 0

    p3dx = 0
    p3dy = 0

    if keys[pygame.K_LEFT]:
        p1dx-=1
        p3dx+=1
    if keys[pygame.K_RIGHT]:
        p1dx+=1
        p3dx-=1
    if keys[pygame.K_UP]:
        p1dy-=1
        p3dy+=1
    if keys[pygame.K_DOWN]:
        p1dy+=1
        p3dy-=1

    if keys[pygame.K_a]:
        p2dx-=1
    if keys[pygame.K_d]:
        p2dx+=1
    if keys[pygame.K_w]:
        p2dy-=1
    if keys[pygame.K_s]:
        p2dy+=1

    player.move(p1dx, p1dy)
    player2.move(p2dx, p2dy)
    player3.move(p3dx, p3dy)
    player.draw(screen)
    player2.draw(screen)
    player3.draw(screen)
    
    pygame.display.flip()

pygame.quit()

