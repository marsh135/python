import pygame
import random
pygame.init()

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf =  pygame.image.load("games/PyGame/sprites/missile.png").convert()
        self.surf.set_colorkey((255,255,255), pygame.RLEACCEL)
        #self.rect =  self.surf.get_rect()
        #self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center=(random.randint(width+20, width+100), random.randint(0, height)))
        self.speed = random.randint(2, 6)
    
    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf =  pygame.image.load("games/PyGame/sprites/jet.png").convert()
        self.surf.set_colorkey((255,255,255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[pygame.K_UP]:
            self.rect.move_ip(0,-5)
        if pressed_keys[pygame.K_DOWN]:
            self.rect.move_ip(0,5)
        if pressed_keys[pygame.K_LEFT]:
            self.rect.move_ip(-5,0)
        if pressed_keys[pygame.K_RIGHT]:
            self.rect.move_ip(5,0)

        #Keep on screen
            
        if self.rect.left <0:
            self.rect.left = 0
        if self.rect.right > width:
            self.rect.right =  width
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= height:
            self.rect.bottom =  height




width = 800
height = 600

screen = pygame.display.set_mode((width, height))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

player1 = Player()

#Create enemies
enemies =  pygame.sprite.Group()
all_sprites =  pygame.sprite.Group()
all_sprites.add(player1)

running =  True

while running:
    for event in pygame.event.get():
        if event.type ==  pygame.QUIT:
            running =  False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == ADDENEMY:
            new_enemy =  Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
    
    screen.fill((0,0,0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player1, enemies):
        player1.kill()
        running = False

    pressed_keys = pygame.key.get_pressed()
    player1.update(pressed_keys)
    enemies.update()

    screen.blit(player1.surf, player1.rect)
    pygame.display.flip()

pygame.quit()
