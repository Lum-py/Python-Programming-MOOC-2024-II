# WRITE YOUR SOLUTION HERE:
import pygame
import math
from datetime import datetime

pygame.init()

display = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Clock")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    center = (display.get_width() // 2, display.get_height() // 2)
    t = datetime.now()

    pygame.draw.circle(display, (255, 0, 0), center, 200, 5)
    pygame.draw.circle(display, (255, 0, 0), center, 10)

    second_angle = 2 * math.pi * t.second / 60 - math.pi / 2
    minute_angle = 2 * math.pi * (t.minute + t.second / 60) / 60 - math.pi / 2
    hour_angle = 2 * math.pi * ((t.hour % 12) + t.minute / 60) / 12 - math.pi / 2

    second_hand = (center[0] + int(180 * math.cos(second_angle)),
                       center[1] + int(180 * math.sin(second_angle)))
    minute_hand = (center[0] + int(160 * math.cos(minute_angle)),
                       center[1] + int(160 * math.sin(minute_angle)))
    hour_hand = (center[0] + int(120 * math.cos(hour_angle)),
                     center[1] + int(120 * math.sin(hour_angle)))

    pygame.draw.line(display, (0, 0, 255), center, second_hand, 2)
    pygame.draw.line(display, (0, 0, 255), center, minute_hand, 4)
    pygame.draw.line(display, (0, 0, 255), center, hour_hand, 6)
   
    pygame.display.flip()
    display.fill((0, 0, 0))
    clock.tick(60)