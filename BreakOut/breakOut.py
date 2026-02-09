import pygame
import ball
import brick
import paddle
import random
import time

RGB = ((255,0,0),(0,255,0),(0,0,255))
BLACK = (0,0,0)
WHITE = (255,255,255)
SCREEN_SIZE = (1280, 720)

#pygame screen initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
running = True
points = 0

paddle = paddle.Paddle(screen,SCREEN_SIZE[0]/2, SCREEN_SIZE[1]-50)
ball = ball.Ball(screen, SCREEN_SIZE[0]/2, SCREEN_SIZE[1]/2, random.choice([-1,1])*random.randint(35,145),1)
bricks= brick.generateBricks(5,10,screen)
font = pygame.font.SysFont(None, 30)

while pygame.time.get_ticks() < 8000:
    screen.fill(BLACK)
    tutorial = font.render('Use left and right arrow keys to move the paddle', True, WHITE)
    screen.blit(tutorial, (SCREEN_SIZE[0]/2 - tutorial.get_width()/2, SCREEN_SIZE[1]/2 - tutorial.get_height()/2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        paddle.move(-1)
    if keys[pygame.K_RIGHT]:
        paddle.move(1)
    paddle.draw()
    pygame.display.flip()
    


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
    if ball.y >= SCREEN_SIZE[1]:
        running=False
        screen.fill(BLACK)
        gameOver = font.render(f'Game Over! Final Score: {points}', True, WHITE)
        screen.blit(gameOver, (SCREEN_SIZE[0]/2 - gameOver.get_width()/2, SCREEN_SIZE[1]/2 - gameOver.get_height()/2))
        pygame.display.flip()
        time.sleep(3)

    paddle.collideBall(ball)
    for i in bricks:
        if i:
            if i.collideBall(ball):
                points += 1
                if points == len(bricks):
                    running = False
                    screen.fill(BLACK)
                    winGame = font.render(f'You Win! Final Score: {points}', True, WHITE)
                    screen.blit(
                        winGame,
                        (SCREEN_SIZE[0]/2 - winGame.get_width()/2, SCREEN_SIZE[1]/2 - winGame.get_height()/2)
                        )
                    pygame.display.flip()
                    time.sleep(3)
            i.draw(screen)

    paddle.draw()
    ball.draw()
    scoreCNT = font.render(f'Score: {points}', True, WHITE)
    screen.blit(scoreCNT, (10, SCREEN_SIZE[1]-30))
    pygame.display.flip()



pygame.quit()
