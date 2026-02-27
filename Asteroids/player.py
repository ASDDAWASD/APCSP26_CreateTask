import pygame
from pygame.math import Vector2
import asteroid
pygame.mixer.init()
PLAYER_DEATH = pygame.USEREVENT + 2

class Player():
    def __init__(self, screen, pos=(0,0), scale = 1):
        self.costumes = [
            pygame.image.load("Asteroids/assets/sprites/spaceship_IDLE.png").convert_alpha(),
            pygame.image.load("Asteroids/assets/sprites/spaceship_MOVING.png").convert_alpha()
            ]
        self.costumes[0] = pygame.transform.scale_by(self.costumes[0], scale)
        self.costumes[1] = pygame.transform.scale_by(self.costumes[1], scale)
        self.scale = scale
        self.size = (self.costumes[0].get_size())
        self.pos = Vector2(pos)
        self.vel = Vector2(0,-1)
        self.accel = Vector2(0,0)
        self.screen = screen
        self.hurtbox = pygame.rect.Rect(0,0,0,0)
        self.lives = 3
        self.immune = 0
        self.hurt = pygame.mixer.Sound("Asteroids/assets/SFX/crash.wav")
        self.thrust = pygame.mixer.Sound("Asteroids/assets/SFX/thrust.wav")
        self.thrust.set_volume(0.5)

    def move(self,controls={"thrust":False, "right":False, "left":False},speed=5,dt=0):
        self.accel*=0
        self.vel*=0.95
        unit=Vector2.normalize(self.vel)*dt*speed
        if controls["thrust"]:
            self.accel=unit
            # self.thrust.play()
        if controls["right"]:
            self.accel+=unit.rotate(90)
        if controls["left"]:
            self.accel+=unit.rotate(-90)
        self.vel+=self.accel
        self.pos+=self.vel
        if self.pos[0] < 0:
            self.pos[0] = self.screen.get_width()
        elif self.pos[0] > self.screen.get_width():
            self.pos[0] = 0
        if self.pos[1] < 0:
            self.pos[1] = self.screen.get_height()
        elif self.pos[1] > self.screen.get_height():
            self.pos[1] = 0

        self.hurtbox = pygame.rect.Rect(self.pos[0]-15,self.pos[1]-15,120*self.scale,120*self.scale)
    
    def draw(self):
        if (self.immune//10)%2:
            return
        dir=180-self.vel.as_polar()[1]
        if self.accel.magnitude() == 0.0:
            self.screen.blit(pygame.transform.rotate(self.costumes[0],dir), (self.pos[0]-(self.size[0]/2),self.pos[1]-(self.size[1]/2)))
        else:
            self.screen.blit(pygame.transform.rotate(self.costumes[1],dir), (self.pos[0]-(self.size[0]/2),self.pos[1]-(self.size[1]/2)))
        # pygame.draw.rect(self.screen,(255,0,0),self.hurtbox,5)

    def collideAsteroid(self):
        if not self.immune:
            for i in asteroid.asteroids:
                if self.hurtbox.colliderect(i.hitbox):
                    self.immune = 120
                    self.lives -= 1
                    self.hurt.play()
        if self.immune > 0:
            self.immune -= 1
        if self.lives == 0:
            pygame.event.post(pygame.event.Event(PLAYER_DEATH))

    def drawLives(self):
        counter = pygame.transform.rotate(pygame.transform.scale_by(self.costumes[0], 0.8),-90)
        for i in range(self.lives):
            self.screen.blit(counter,(((self.size[1]*0.8)+5)*i,((self.size[0]*0.8)/2)))