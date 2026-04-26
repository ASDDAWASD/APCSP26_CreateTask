import pygame
from pygame.math import Vector2

pygame.mixer.init()
bullets=[]
ammo = 5
SFX_shoot = pygame.mixer.Sound("assets/SFX/laserShoot.wav")
channel = pygame.mixer.Channel(2)

class Bullet():
    def __init__(self,screen,pos,vel):
        self.idx = len(bullets) # index in bullets list acts as a unique identifier for each bullet
        self.screen = screen
        self.pos = Vector2(pos)
        self.vel = vel
        channel.play(SFX_shoot)


    def move(self):
        self.pos+=self.vel
        if (
            self.pos[0] < 0 or
            self.pos[1] < 0 or
            self.pos[0] > self.screen.get_width() or
            self.pos[1] > self.screen.get_height()
            ):
            for i in bullets: # update the indices of each existing bullet to account for the removal of this bullet
                if i.idx > self.idx:
                    i.idx-=1
            bullets.pop(self.idx) # remove the bullet from the list of bullets if it goes off screen

    def draw(self):
        pygame.draw.circle(self.screen,(255,255,255),self.pos,2)