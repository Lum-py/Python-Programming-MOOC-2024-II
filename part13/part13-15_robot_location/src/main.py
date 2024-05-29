# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = randint(0, 640 - robot.get_width())
y = randint(0, 480 - robot.get_height())

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            center_x = x + robot.get_width() /2
            center_y = y + robot.get_height() / 2 

            if abs(mouse_x - center_x) < robot.get_width() / 2 and abs(mouse_y - center_y) < robot.get_height() / 2:
                    x = randint(0, 640 - robot.get_width())
                    y = randint(0, 480 - robot.get_height())
            

            window.fill((0, 0, 0))
            window.blit(robot, (x, y))
            pygame.display.flip()

        if event.type == pygame.QUIT:
            exit()