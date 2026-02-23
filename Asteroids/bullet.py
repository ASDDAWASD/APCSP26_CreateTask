import pygame
from pygame.math import Vector2

pygame.mixer.init()
bullets=[]
shoot= pygame.mixer.Sound("Asteroids/assets/SFX/laserShoot.wav")

class Bullet():
    def __init__(self,surface,pos,vel):
        self.surface = surface
        self.pos = Vector2(pos)
        self.vel = vel
        shoot.play()


    def move(self):
        self.pos+=self.vel

    def draw(self):
        pygame.draw.circle(self.surface,(255,255,255),self.pos,2)