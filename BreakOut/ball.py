import pygame
import math

class Ball:
    def __init__(self,screen,x,y,dir=1,speed=1):
        self.vel = 0
        self.x = x
        self.y = y
        self.radius = 10
        self.hitbox = pygame.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)
        self.vel =[math.cos(math.radians(dir))*speed,math.sin(math.radians(dir))*speed]
        self.screen = screen

    def move(self):
        self.x += self.vel[0]
        self.y += self.vel[1]
        if self.x <= 0 or self.x >= self.screen.get_width()-self.radius:
            self.vel[0] = 0-self.vel[0]
            self.x = max(0,min(self.x,self.screen.get_width()-self.radius))
        if self.y <= 0 or self.y >= self.screen.get_height()-self.radius:
            self.vel[1] = 0-self.vel[1]
            self.y = max(0,min(self.y,self.screen.get_height()-self.radius))
        self.hitbox = pygame.Rect(self.x-self.radius, self.y-self.radius, self.radius*2, self.radius*2)
        

    def draw(self):
        pygame.draw.circle(self.screen, (255,255,255), (int(self.x), int(self.y)), self.radius)
