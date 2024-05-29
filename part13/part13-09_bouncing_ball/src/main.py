# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()
window = pygame.display.set_mode((640, 480))

ball = pygame.image.load("ball.png")

x = 0
y = 0
x_velocity = 5
y_velocity = 5
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()

    y += y_velocity
    x += x_velocity
    if x + ball.get_width() > 640 or x <= 0:
        x_velocity *= -1
    if y + ball.get_height() > 480 or y <= 0:
        y_velocity *= -1
    

    clock.tick(60)