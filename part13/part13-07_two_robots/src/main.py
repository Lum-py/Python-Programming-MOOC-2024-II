# WRITE YOUR SOLUTION HERE:
import pygame
pygame.init()
window = pygame.display.set_mode((640, 480))

robots = [pygame.image.load("robot.png"), pygame.image.load("robot.png")]

positions = [(0, 50), (0, 150)]
velocities = [1, 2]

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))    
    
    for i in range(len(robots)):
        window.blit(robots[i], positions[i])
        
        positions[i] = (positions[i][0] + velocities[i], positions[i][1])

        if velocities[i] > 0 and positions[i][0] + robots[i].get_width() >= 640:
            velocities[i] = - velocities[i]
        elif velocities[i] < 0 and positions[i][0] <= 0:
            velocities[i] = - velocities[i]
    pygame.display.flip()
        
    


    clock.tick(60)