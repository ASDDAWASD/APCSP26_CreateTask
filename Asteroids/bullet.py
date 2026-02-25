import pygame
from pygame.math import Vector2

pygame.mixer.init()
bullets=[]
shoot = pygame.mixer.Sound("Asteroids/assets/SFX/laserShoot.wav")

class Bullet():
    def __init__(self,screen,pos,vel):
        self.idx = len(bullets)
        self.screen = screen
        self.pos = Vector2(pos)
        self.vel = vel
        shoot.play()


    def move(self):
        self.pos+=self.vel
        if (
            self.pos[0] < 0 or
            self.pos[1] < 0 or
            self.pos[0] > self.screen.get_width() or
            self.pos[1] > self.screen.get_height()
            ):
            for i in bullets:
                if i.idx > self.idx:
                    i.idx-=1
            bullets.pop(self.idx)

    def draw(self):
        pygame.draw.circle(self.screen,(255,255,255),self.pos,2)