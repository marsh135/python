import pygame

from pygame.locals import(K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE, KEYDOWN, QUIT)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player,self).__init__()
        self.surf =  pygame.Surface((75,25))
        self.surf.fill((255,255,255))
        self.rect =  self.surf.get_rect()
    
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
             self.rect.move_ip(0, -1)
        if pressed_keys[K_DOWN]:
             self.rect.move_ip(0, 1)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 1)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 1)

pygame.init()

width = 800
height = 600

screen = pygame.display.set_mode((width, height))


player = Player()


running =  True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running= False
        elif event.type ==  pygame.QUIT:
            running =  False
    pygame.display.flip()

    pressed_keys =  pygame.key.get_pressed()

    player.update(pressed_keys)
    screen.fill((0,0, 0))

  
    screen.blit(player.surf, player.rect)
    pygame.display.flip()

#pygame.quit()

