import pygame
import random
from pygame.math import Vector2

asteroids=[]


class Asteroid():
    def __init__(self,screen,pos,vel,scale=1):
        self.idx = len(asteroids)
        self.screen = screen
        self.scale = scale
        self.sprite = pygame.image.load(f"Asteroids/assets/sprites/asteroid_{random.randint(1,2)}.png").convert_alpha()
        self.sprite = pygame.transform.scale_by(self.sprite,scale)
        self.pos = Vector2(pos)
        self.vel = Vector2(vel)
        self.hitbox = pygame.Rect(self.pos[0]-(100*scale),self.pos[1]-(100*scale),200*scale,200*scale)
        

    def move(self):
        self.pos+=self.vel
        self.hitbox = pygame.Rect(self.pos[0]-100,self.pos[1]-100,200,200)
        if (
            self.pos[0] < (0-self.scale*600) or
            self.pos[1] < (0-self.scale*600) or
            self.pos[0] > (self.screen.get_width()+self.scale*300) or
            self.pos[1] > (self.screen.get_height()+self.scale*300)
            ):
            for i in asteroids:
                if i.idx > self.idx:
                    i.idx-=1
            asteroids.pop(self.idx)

    def draw(self):
        self.screen.blit(self.sprite, self.pos)