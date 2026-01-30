import pygame
import random

bricks = []

class Brick:
    def __init__(self, rect, idx):
        self.hitbox = rect
        self.color = random.choice(((255,0,0),(0,255,0),(0,0,255)))
        self.idx = idx

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.hitbox)

    def collideBall(self,ball):
        for i in range(4):
            if self.hitbox.collidepoint(ball.hitpoints[i]):
                bricks[self.idx]=False
                if(i==0 or i==1):
                    ball.vel[0] = 0-ball.vel[0]
                    return True
                else:
                    ball.vel[1] = 0-ball.vel[1]
                return True
            return False
    
def generateBricks(rows,cols,screen):
    brickWidth = (0.9*screen.get_width())/cols
    brickHeight = (0.9*screen.get_height())/(2*rows)
    margin=((0.1*screen.get_width()/cols),(0.1*screen.get_height()/rows))
    for i in range(rows):
        for j in range(cols):
            bricks.append(Brick(pygame.Rect(j*(brickWidth + margin[0]), i*(brickHeight + margin[1]), brickWidth, brickHeight),((i*cols)+j)))
    return bricks
