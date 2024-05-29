# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")
 
screen.fill((0, 0, 0))
width = robot.get_width()
height = robot.get_height()
for r in range(1000):
    x = randint(0, 640-width)
    y = randint(0 , 480-height)
    screen.blit(robot, (x, y))

pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()