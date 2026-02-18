import pygame
from pygame.math import Vector2
import math

class Player():
    def __init__(self, screen, pos=(0,0), scale = 1):
        self.costumes = [
            pygame.image.load("Asteroids/assets/sprites/spaceship_IDLE.png").convert_alpha(),
            pygame.image.load("Asteroids/assets/sprites/spaceship_MOVING.png").convert_alpha()
            ]
        self.costumes[0] = pygame.transform.scale_by(self.costumes[0], scale)
        self.costumes[1] = pygame.transform.scale_by(self.costumes[1], scale)
        self.size = (self.costumes[0].get_size())
        self.pos = Vector2(pos)
        self.vel = Vector2(0,-1)
        self.accel = Vector2(0,0)
        self.screen = screen
        

    def move(self,controls={"thrust":False, "right":False, "left":False},speed=10,dt=0):
        self.accel*=0
        self.vel*=0.95
        unit=Vector2.normalize(self.vel)*dt*speed
        if controls["thrust"]:
            self.accel=unit
        if controls["right"]:
            self.accel+=unit.rotate(90)
        if controls["left"]:
            self.accel+=unit.rotate(-90)
        self.vel+=self.accel
        self.pos+=self.vel
    
    def draw(self):
        dir=180-self.vel.as_polar()[1]
        if self.accel.magnitude() == 0.0:
            self.screen.blit(pygame.transform.rotate(self.costumes[0],dir), (self.pos[0]-(self.size[0]/2),self.pos[1]-(self.size[1]/2)))
        else:
            self.screen.blit(pygame.transform.rotate(self.costumes[1],dir), (self.pos[0]-(self.size[0]/2),self.pos[1]-(self.size[1]/2)))
