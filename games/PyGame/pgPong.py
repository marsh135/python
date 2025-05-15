import pygame
pygame.init()

scoreFont =  pygame.font.Font('freesansbold.ttf', 20)

class Paddle:
    def __init__(self, x, y,speed, h, w, rgb):
        self.x =  x
        self.y = y
        self.speed = speed
        self.h =  h
        self.w =  w
        self.rgb = rgb
        #create the paddle
        self.paddleRect =  pygame.Rect(x,y,w,h)
        #put it on the screen
        self.paddle =  pygame.draw.rect(screen, self.rgb, self.paddleRect)
    def display(self):
        self.paddle =  pygame.draw.rect(screen, self.rgb, self.paddleRect)
    def update(self, yDir):
        #if yDir = 1, moving up
        #if yDir =  -1, moving down
        #if yDir = 0, not moving
        self.y = self.y + self.speed*yDir
        if self.y <0:
            self.y = 0
        elif self.y  + self.h >= SCREEN_HEIGHT:
            self.y = SCREEN_HEIGHT - self.h
        self.paddleRect = (self.x, self.y, self.w, self.h)
    
    def displayScore(self, text, score, x, y, color):
        text = scoreFont.render(text+str(score), True, color)
        textRect =  text.get_rect()
        textRect.center = (x,y)

        screen.blit(text, textRect)

    def getRect(self):
        return self.paddleRect

class Ball:
    def __init__(self, xpos, ypos, speed, radius, color):
        self.xpos =  xpos
        self.ypos = ypos
        self.speed = speed
        self.radius =  radius
        self.color =  color

        self.xFac =  1
        self.yFac = -1

        self.ball =  pygame.draw.circle(
            screen, self.color, (self.xpos, self.ypos), self.radius)
        
        self.firstPlay = 1
    
    def display(self):
        self.ball = pygame.draw.circle(
            screen, self.color, (self.xpos, self.ypos), self.radius)

    def update(self):
        self.xpos += self.speed*self.xFac
        self.ypos +=  self.speed*self.yFac

        if self.ypos <=0  or self.ypos>= SCREEN_HEIGHT:
            self.yFac = self.yFac* -1

        if self.xpos <0 and self.firstPlay:
            self.firstPlay = 0
            return 1
        elif self.xpos >= SCREEN_WIDTH and self.firstPlay:
            self.firstPlay = 0
            return -1
        else:
            return 0
    
    def reset(self):
        self.xpos =  SCREEN_WIDTH//2
        self.ypos =  SCREEN_HEIGHT//2
        self.xFac *=-1
        self.yFac *=1
        self.firstPlay = 1

    def hit(self):
        self.xFac = self.xFac * -1

        #Shorter, but still good
        #self.xFac *= -1

    def getBall(self):
        return self.ball

SCREEN_WIDTH =  800
SCREEN_HEIGHT = 600

clock = pygame.time.Clock()
FPS = 30

RED = (255,0,0)
BLUE = (0,0, 255)
WHITE = (255,255,255)
BLACK =  (0,0,0)
screen =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PONG!")

#create paddles
paddleRed =  Paddle(20, SCREEN_HEIGHT//2-50, 7, 100, 10, RED)
paddleBlue =  Paddle(SCREEN_WIDTH-30, SCREEN_HEIGHT//2-50, 7, 100, 10, BLUE)

paddleList = [paddleRed, paddleBlue]

#create ball
ball =  Ball(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 7, 7, WHITE)

running =  True

paddle1YFac = 0
paddle2YFac = 0

redScore = 0
blueScore =  0


while running:

    screen.fill(BLACK)

    #Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key ==  pygame.K_UP:
                paddle2YFac = -1
            if event.key ==  pygame.K_DOWN:
                paddle2YFac = 1
            if event.key ==  pygame.K_w:
                paddle1YFac = -1
            if event.key ==  pygame.K_s:
                paddle1YFac = 1
            if event.key ==  pygame.K_ESCAPE:
                running =  False
        if event.type == pygame.KEYUP:
            if event.key ==  pygame.K_UP: # and paddle2YFac ==1
                paddle2YFac = 0
            if event.key ==  pygame.K_DOWN:
                paddle2YFac = 0
            if event.key ==  pygame.K_w:
                paddle1YFac = 0
            if event.key ==  pygame.K_s:
                paddle1YFac = 0
            
    for paddle in paddleList:
        if pygame.Rect.colliderect(ball.getBall(), paddle.getRect()):
           ball.hit()

    paddleRed.update(paddle1YFac)
    paddleBlue.update(paddle2YFac)
    point = ball.update()

    if point == -1:
        redScore+=1
    elif point == 1:
        blueScore+=1
    
    if point:
        ball.reset()

    paddleRed.display()
    paddleBlue.display()
    ball.display()

    paddleRed.displayScore("Red Score: ", redScore, 100, 20, WHITE)
    paddleBlue.displayScore("Blue Score: ", blueScore, SCREEN_WIDTH-100, 20, WHITE)



    pygame.display.update()
    clock.tick(FPS)


pygame.quit()