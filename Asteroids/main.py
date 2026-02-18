import pygame
import asteroid
import player

BLACK = (0,0,0)
WHITE = (255,255,255)

SCREEN_SIZE = (800, 800)

#pygame screen initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
running = True
points = 0

#intialize clock for DT
clock=pygame.time.Clock()
FPS = 60
dt=clock.tick(FPS)/1000

#initialize player
player = player.Player(screen, (SCREEN_SIZE[0]/2,SCREEN_SIZE[1]/2), 0.4)

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    #move objects
    player.move({
        "thrust":keys[pygame.K_UP],
        "right":keys[pygame.K_RIGHT],
        "left":keys[pygame.K_LEFT]
        },15,dt)

    #draw sprites
    player.draw()

    pygame.display.flip()

    #clock tick
    dt=clock.tick(FPS)/1000
pygame.quit()
