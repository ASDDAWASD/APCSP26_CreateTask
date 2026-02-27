import pygame
import asteroid
import player
import bullet
import random
import time

BLACK = (0,0,0)
WHITE = (255,255,255)

SCREEN_SIZE = (800, 800)

#pygame screen initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
running = True
points = 0
font = pygame.font.Font("Asteroids/assets/fonts/Minecraft.ttf",60) #font source: https://www.dafont.com/minecraft.font
points = 0

#intialize clock for DT
clock=pygame.time.Clock()
FPS = 60
dt=clock.tick(FPS)/1000

def makeAsteroid(scale=1,speed=1):
    spawnx = random.random()*SCREEN_SIZE[0]
    spawny = random.random()*SCREEN_SIZE[1]
    velx = random.uniform(-1,1)*speed
    vely = random.uniform(-1,1)*speed
    while True:
        spawnx-=velx
        spawny-=vely
        if (
            spawnx < (0-scale*300) or
            spawny < (0-scale*300) or
            spawnx > SCREEN_SIZE[0]+scale or
            spawny > SCREEN_SIZE[1]+scale
            ):
            break
    
    asteroid.asteroids.append(asteroid.Asteroid(screen,(spawnx,spawny),(velx,vely),scale))

def shoot():
    bullet.bullets.append(bullet.Bullet(screen,player.pos,player.vel+(10*player.vel.normalize())))


#initialize player
player = player.Player(screen, (SCREEN_SIZE[0]/2,SCREEN_SIZE[1]/2), 0.4)

MAKE_ASTEROID = pygame.USEREVENT + 1
PLAYER_DEATH = pygame.USEREVENT + 2
pygame.time.set_timer(MAKE_ASTEROID,8000)

#instructions screen
check={pygame.K_UP:0,pygame.K_RIGHT:0,pygame.K_LEFT:0,pygame.K_SPACE:0}
instructions = pygame.font.Font("Asteroids/assets/fonts/Minecraft.ttf",30).render("Use arrow keys to move and space to shoot.",True,WHITE)
while running and 0 in check.values():
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot()
                check[pygame.K_SPACE]=1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        check[pygame.K_UP] = 1
    if keys[pygame.K_RIGHT]:
        check[pygame.K_RIGHT] = 1
    if keys[pygame.K_LEFT]:
        check[pygame.K_LEFT] = 1

    #move objects
    player.move({
        "thrust":keys[pygame.K_UP],
        "right":keys[pygame.K_RIGHT],
        "left":keys[pygame.K_LEFT]
        },15,dt)
    for i in bullet.bullets:
        i.move()

    #draw objects
    player.draw()
    for i in bullet.bullets:
        i.draw()
    screen.blit(instructions,((SCREEN_SIZE[0]-(instructions.get_width()))/2, 10))

    pygame.display.flip()
    #clock tick
    dt=clock.tick(FPS)/1000

#initialize asteroids
for i in range(5):
    makeAsteroid(scale=0.5,speed=0.5)

#main game loop
while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shoot()
        if event.type == MAKE_ASTEROID:
            makeAsteroid(scale=0.5,speed=0.5)
        if event.type == PLAYER_DEATH:
            running = False

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
        i.move()
    

    #check collisions
    for i in asteroid.asteroids:
        for j in bullet.bullets:
            check = i.collideBullet(j)
            if check:
                points += check
    player.collideAsteroid()
    print(player.lives)
    
    #draw sprites
    player.draw()
    for i in bullet.bullets:
        i.draw()
    for i in asteroid.asteroids:
        i.draw()
    player.drawLives()
    score = font.render(str(points),True,WHITE)
    screen.blit(score,(10, SCREEN_SIZE[1]-(score.get_height())))

    pygame.display.flip()

    #clock tick
    dt=clock.tick(FPS)/1000

#fade screen out
fader = pygame.Surface(SCREEN_SIZE,pygame.SRCALPHA)
for i in range(256):
    fader.fill((0,0,0,i))
    screen.blit(fader,(0,0))

    pygame.display.flip()
    dt=clock.tick(FPS)/1000

#display game over screen
screen.fill(BLACK)
score = font.render(f"Game Over! Score: {str(points)}",True,WHITE)

#fade in game over screen
for i in range(256):
    score.set_alpha(i)
    screen.blit(score,((SCREEN_SIZE[0]-score.get_width())/2,(SCREEN_SIZE[1]-score.get_height())/2))

    pygame.display.flip()
    dt=clock.tick(FPS)/1000


time.sleep(2)
pygame.quit()
