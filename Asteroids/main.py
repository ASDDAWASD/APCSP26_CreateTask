import pygame
import asteroid
import player
import bullet
import random

BLACK = (0,0,0)
WHITE = (255,255,255)

SCREEN_SIZE = (800, 800)

#pygame screen initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
running = True
points = 0
font = pygame.font.Font("Asteroids/assets/fonts/Minecraft.ttf",30) #font source: https://www.dafont.com/minecraft.font
points = 0

#intialize clock for DT
clock=pygame.time.Clock()
FPS = 60
dt=clock.tick(FPS)/1000

#initialize player
player = player.Player(screen, (SCREEN_SIZE[0]/2,SCREEN_SIZE[1]/2), 0.4)
for i in range(5):
    asteroid.asteroids.append(asteroid.Asteroid(screen,(random.random()*SCREEN_SIZE[0],random.random()*SCREEN_SIZE[1])))

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet.bullets.append(bullet.Bullet(screen,player.pos,player.vel+(10*player.vel.normalize())))
                points += 1
    keys = pygame.key.get_pressed()


    #move objects
    player.move({
        "thrust":keys[pygame.K_UP],
        "right":keys[pygame.K_RIGHT],
        "left":keys[pygame.K_LEFT]
        },15,dt)

    for i in bullet.bullets:
        i.move()
    for i in asteroid.asteroids:
        i.move

    #draw sprites
    player.draw()
    for i in bullet.bullets:
        i.draw()
    for i in asteroid.asteroids:
        i.draw()
    score = font.render(str(points),True,WHITE)
    screen.blit(score,(10, SCREEN_SIZE[1]-(score.get_height())-5))

    pygame.display.flip()

    #clock tick
    dt=clock.tick(FPS)/1000
pygame.quit()
