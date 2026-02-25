import pygame
import random
import bullet
from pygame.math import Vector2

pygame.mixer.init()
asteroids=[]
SFX_pop = [pygame.mixer.Sound("Asteroids/assets/SFX/explosion_1.wav")]

MAKE_ASTEROID = pygame.USEREVENT + 1

class Asteroid():
    def __init__(self,screen,pos,vel,scale=1,type=3):
        self.idx = len(asteroids)
        self.screen = screen
        self.scale = scale
        self.sprite = pygame.image.load(f"Asteroids/assets/sprites/asteroid_{random.randint(1,2)}.png").convert_alpha()
        self.sprite = pygame.transform.scale_by(self.sprite,scale)
        self.pos = Vector2(pos)
        self.vel = Vector2(vel)
        self.hitbox = pygame.Rect(self.pos[0]+(100*scale),self.pos[1]+(100*scale),200*scale,200*scale)
        self.type = type
        

    def move(self):
        self.pos+=self.vel
        self.hitbox = pygame.Rect(self.pos[0]+(50*self.scale),self.pos[1]+(50*self.scale),200*self.scale,200*self.scale)
        if (
            self.pos[0] < (0-self.scale*600) or
            self.pos[1] < (0-self.scale*600) or
            self.pos[0] > (self.screen.get_width()+self.scale*300) or
            self.pos[1] > (self.screen.get_height()+self.scale*300)
            ):
            print(len(asteroids),self.idx)
            for i in asteroids:
                if i.idx > self.idx:
                    i.idx-=1
            asteroids.pop(self.idx)

    def draw(self):
        self.screen.blit(self.sprite, self.pos)
        pygame.draw.rect(self.screen,(255,0,0),self.hitbox,5)

    def collideBullet(self,checkbullet):
        if self.hitbox.collidepoint(checkbullet.pos):
            for i in asteroids:
                if i.idx > self.idx:
                    i.idx-=1
            for i in bullet.bullets:
                if i.idx>checkbullet.idx:
                    i.idx-=1
            aux=self
            bullet.bullets.pop(checkbullet.idx)
            asteroids.pop(self.idx)


            if aux.type > 1:
                for i in range(aux.type):
                    asteroids.append(Asteroid(
                        aux.screen,
                        (aux.pos[0]+random.uniform(-5,5),aux.pos[1]+random.uniform(-5,5)),
                        (random.uniform(-1,1)*aux.vel[0]*aux.type,random.uniform(-1,1)*aux.vel[0]*aux.type),
                        aux.scale/aux.type,
                        1
                    ))
                pygame.event.post(pygame.event.Event(MAKE_ASTEROID))
           
            SFX_pop[random.randint(0,len(SFX_pop)-1)].play()
            return aux.type
        return 0