# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

velocity = 0.01

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    for i in range(10):
        angle = i * (2 * math.pi / 10) + velocity
        x = 320+math.cos(angle)*140 - robot.get_width() / 2
        y = 240+math.sin(angle)*140 - robot.get_height() / 2        
        window.blit(robot, (x, y))
        
    pygame.display.flip()
    velocity += 0.01
    
    clock.tick(60)