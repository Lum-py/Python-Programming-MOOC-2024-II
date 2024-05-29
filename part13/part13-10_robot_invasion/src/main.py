# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

robots = []

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    if random.randint(1, 80) == 1:
        x = random.randint(0, 640 - robot.get_width())
        y = 0 - robot.get_height()
        z = random.choice([1, -1])
        robots.append((x, y, z))

    window.fill((0, 0, 0))

    for i in range(len(robots))[::-1]:
        x, y, z = robots[i]
        y += 1

        if y >= 480 - robot.get_height():
            y = 480 - robot.get_height()
            x += z            
            if x < 0 - robot.get_width() or x > 640 + robot.get_width():
                del robots[i]
            else:
              robots[i] = (x, y, z)
        else:
          robots[i] = (x, y, z)
        window.blit(robot, (x, y))
  

    pygame.display.flip()

    clock.tick(60)
