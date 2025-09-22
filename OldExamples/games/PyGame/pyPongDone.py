import pygame
pygame.init()

font20 = pygame.font.Font('freesansbold.ttf', 20)

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
    def getRect(self):
        return self.paddleRect
    
    

    def displayScore(self, text, score, x, y, color):
        text = font20.render(text+str(score), True, color)
        textRect = text.get_rect()
        textRect.center = (x, y)
 
        screen.blit(text, textRect)

class Ball:

    def __init__(self, bx, by, br, bs, bc):
        self.bx =  bx
        self.by =  by
        self.br =  br
        self.bs =  bs
        self.bc =  bc
        self.xFac = 1
        self.yFac = -1
        self.firstTime = 1

        self.ball =  pygame.draw.circle(screen, self.bc, (self.bx, self.by), self.br)

    def display(self):
        self.ball =  pygame.draw.circle(screen, self.bc, (self.bx, self.by), self.br)

    def update(self):
        self.bx += self.bs*self.xFac
        self.by += self.bs*self.yFac

        if self.by <0 or self.by >= SCREEN_HEIGHT:
            self.yFac *=-1

        if self.bx <0 and self.firstTime:
            self.firstTime = 0
            return 1
        elif self.bx >= SCREEN_WIDTH and self.firstTime:
            self.firstTime = 0
            return -1
        else:
            return 0
        
    def reset(self):
        self.bx =  SCREEN_WIDTH//2
        self.by = SCREEN_HEIGHT//2

        self.xFac *=-1
        self.firstTime = 1

    def hit(self):
        self.xFac *=-1
    
    def getRect(self):
        return self.ball

        


SCREEN_WIDTH =  800
SCREEN_HEIGHT = 600

clock = pygame.time.Clock()

RED = (255,0,0)
BLUE = (0,0, 255)
WHITE = (255,255,255)
BLACK =  (0,0,0)
FPS = 30
screen =  pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PONG!")



def main():
    running =  True

    #create paddles
    paddleRed =  Paddle(20, 250, 10, 100, 10, RED)
    paddleBlue =  Paddle(SCREEN_WIDTH-30, 250, 10, 100, 10, BLUE)

    #scores
    redScore, blueScore =0,0

    ball = Ball(SCREEN_WIDTH//2, SCREEN_HEIGHT//2, 7, 7, WHITE)

    paddleList = [paddleBlue, paddleRed]


    paddle1YFac = 0
    paddle2YFac = 0

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
                if event.key ==  pygame.K_UP:
                    paddle2YFac = 0
                if event.key ==  pygame.K_DOWN:
                    paddle2YFac = 0
                if event.key ==  pygame.K_w:
                    paddle1YFac = 0
                if event.key ==  pygame.K_s:
                    paddle1YFac = 0

        for paddle in paddleList:
            if pygame.Rect.colliderect(ball.getRect(), paddle.getRect()):

                ball.hit()
                
        paddleRed.update(paddle1YFac)
        paddleBlue.update(paddle2YFac)
        point = ball.update()

        if point == -1:
            redScore +=1
        elif point == 1:
            blueScore+=1

        if redScore == 5:
            pygame.display.update()
            paddleRed.displayScore("Red Wins!  ", redScore, 300,20, WHITE)
        elif blueScore == 5:
            pygame.display.update()
            paddleBlue.displayScore("Blue Wins! ", blueScore, 300,20, WHITE)
        else:

            if point:
                ball.reset()

        paddleRed.display()
        paddleBlue.display()
        ball.display()
        paddleRed.displayScore("Red Score : ", redScore, 100,20, WHITE)
        paddleBlue.displayScore("Blue Score : ", blueScore, SCREEN_WIDTH-100,20, WHITE)
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
    pygame.quit()