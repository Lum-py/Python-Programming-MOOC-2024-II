# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

player_1 = pygame.image.load("robot.png")
x_1, y_1 = 3 * window.get_width() / 4, window.get_height() / 2 - player_1.get_height()
player_2 = pygame.image.load("robot.png")
x_2, y_2 = window.get_width() / 4 - player_2.get_width(), window.get_height() / 2 - player_2.get_height()

to_right1, to_left1, to_top1, to_bottom1 = False, False, False, False
to_right2, to_left2, to_top2, to_bottom2 = False, False, False, False
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left1 = True
            if event.key == pygame.K_RIGHT:
                to_right1 = True
            if event.key == pygame.K_DOWN:
                to_bottom1 = True
            if event.key == pygame.K_UP:
                to_top1 = True
            if event.key == pygame.K_w:
                to_top2 = True
            if event.key == pygame.K_s:
                to_bottom2 = True
            if event.key == pygame.K_a:
                to_left2 = True
            if event.key == pygame.K_d:
                to_right2 = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left1 = False
            if event.key == pygame.K_RIGHT:
                to_right1 = False
            if event.key == pygame.K_DOWN:
                to_bottom1 = False
            if event.key == pygame.K_UP:
                to_top1 = False
            if event.key == pygame.K_w:
                to_top2 = False
            if event.key == pygame.K_s:
                to_bottom2 = False
            if event.key == pygame.K_a:
                to_left2 = False
            if event.key == pygame.K_d:
                to_right2 = False

        if event.type == pygame.QUIT:
            exit()

    if to_right1 and x_1 <= 640 - player_1.get_width():
        x_1 += 2
    if to_left1 and x_1 > 0:
        x_1 -= 2
    if to_top1 and y_1 > 0:
        y_1 -= 2
    if to_bottom1 and y_1 <= 480 - player_1.get_height():
        y_1 += 2 
    
    if to_right2 and x_2 <= 640 - player_2.get_width():
        x_2 += 2
    if to_left2 and x_2 > 0:
        x_2 -= 2
    if to_top2 and y_2 > 0:
        y_2 -= 2
    if to_bottom2 and y_2 <= 480 - player_2.get_height():
        y_2 += 2 

    window.fill((0, 0, 0))
    window.blit(player_1, (x_1, y_1))
    window.blit(player_2, (x_2, y_2))
    pygame.display.flip()

    clock.tick(60)