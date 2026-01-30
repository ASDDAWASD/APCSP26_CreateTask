import pygame

class Paddle:
    def __init__(self,screen,x,y):
        self.vel = 0
        self.x = x
        self.y = y
        self.screen = screen
        self.length = 100
        self.width = 10
        self.hitbox = pygame.Rect(self.x, self.y, self.length, self.width)

    def move(self, dx):
        self.x += dx
        self.x = max(0,min(self.x,self.screen.get_width()-100))
        self.hitbox = pygame.Rect(self.x, self.y, self.length, self.width)

    def draw(self,):
        pygame.draw.rect(self.screen, (255,255,255), self.hitbox)
    
    def collideBall(self,ball):
        if self.hitbox.colliderect(ball.hitbox):
            return True
        return False

