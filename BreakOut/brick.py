import pygame

class Brick:
    def __init__(self, rect):
        self.hitbox = rect

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255), self.hitbox)

def generateBricks(rows,cols,screen):
    bricks = []
    brickWidth = (0.9*screen.get_width())/cols
    brickHeight = (0.9*screen.get_height())/(2*rows)
    margin=((0.1*screen.get_width()/cols),(0.1*screen.get_height()/rows))
    for i in range(rows):
        for j in range(cols):
            bricks.append(Brick(pygame.Rect(j*brickWidth + margin[0], i*brickHeight + margin[1], brickWidth, brickHeight)))
    return bricks