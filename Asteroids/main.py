import pygame
import asteroid
import player

BLACK = (0,0,0)
WHITE = (255,255,255)

SCREEN_SIZE = (720, 720)

#pygame screen initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
running = True
points = 0

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()


    pygame.display.flip()
pygame.quit()
