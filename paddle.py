import pygame

class Paddle:
    def __init__(self,screen,x,y):
        self.vel = 0
        self.x = x
        self.y = y
        self.screen = screen

    def move(self, dx):
        self.x += dx
        self.x = max(0,min(self.x,self.screen.get_width()-100))

    def draw(self,):
        pygame.draw.rect(self.screen, (255,255,255), pygame.Rect(self.x, self.y, 100, 20))