import pygame

class Player():
    def __init__(self, screen, pos=(0,0), scale = 1):
        self.costumes = [
            pygame.image.load("Asteroids/assets/sprites/spaceship_IDLE.png").convert_alpha(),
            pygame.image.load("Asteroids/assets/sprites/spaceship_MOVING.png").convert_alpha()
            ]
        self.costumes[0] = pygame.transform.scale_by(self.costumes[0], scale)
        self.costumes[1] = pygame.transform.scale_by(self.costumes[1], scale)
        self.size = (self.costumes[0].get_size())
        self.pos = pygame.math.Vector2(pos)
        self.vel = pygame.math.Vector2(0,0)
        self.accel = pygame.math.Vector2(0,0)
        self.screen = screen
        

    def move(self):
        pass

    def draw(self):
        if self.accel.magnitude() == 0.0:
            self.screen.blit(self.costumes[0], (self.pos[0]-(self.size[0]/2),self.pos[1]-(self.size[1]/2)))
        else:
            self.screen.blit(self.costumes[1], (self.pos[0]-(self.size[0]/2),self.pos[1]-(self.size[1]/2)))
