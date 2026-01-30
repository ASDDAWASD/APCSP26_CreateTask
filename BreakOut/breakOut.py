import pygame
import ball
import brick
import paddle
import random

RGB = ((255,0,0),(0,255,0),(0,0,255))
BLACK = (0,0,0)
WHITE = (255,255,255)
SCREEN_SIZE = (1280, 720)

#pygame screen initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
running = True

paddle = paddle.Paddle(screen,SCREEN_SIZE[0]/2, SCREEN_SIZE[1]-50)
ball = ball.Ball(screen, SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2, random.choice([-1,1])*random.randint(35,145),1)
bricks= brick.generateBricks(5,10,screen)

while running:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move(-1)
    if keys[pygame.K_RIGHT]:
        paddle.move(1)

    ball.move()
    paddle.collideBall(ball)
    for i in bricks:
        if i:
            i.collideBall(ball)
            i.draw(screen)

    paddle.draw()
    ball.draw()

    pygame.display.flip()



pygame.quit()
