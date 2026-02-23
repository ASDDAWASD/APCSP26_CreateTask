import pygame
import random
from pygame.math import Vector2

asteroids=[]

class Asteroid():
    def __init__(self,screen,pos):
        self.screen = screen
        self.sprite = pygame.image.load(f"Asteroids/assets/sprites/asteroid_{random.randint(1,2)}.png").convert_alpha()
        self.pos = pos
        self.vel = Vector2(random.random()*5, random.random()*5)
        self.hitbox = pygame.Rect(self.pos[0]-100,self.pos[1]-100,200,200)
        

    def move(self):
        self.pos+=self.vel
        self.hitbox = pygame.Rect(self.pos[0]-100,self.pos[1]-100,200,200)

    def draw(self):
        self.screen.blit(self.sprite, self.pos)