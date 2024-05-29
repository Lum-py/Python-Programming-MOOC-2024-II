# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

# window
pygame.init()
window = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Asteroids")

# initialize needed variables and items
rock = pygame.image.load("rock.png")
robot = pygame.image.load("robot.png")

font = pygame.font.SysFont("Courier", 24)

x = window.get_width() // 2 - robot.get_width() / 2
y = 480 - robot.get_height()
score = 0
rocks = []

to_right = False
to_left = False

clock = pygame.time.Clock()

# gameloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    # robot handling
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False    

    if to_right and x <= 640 - robot.get_width():
        x += 4
    if to_left and x > 0:
        x -= 4

    # randomize rock positions (not to fast)
    if randint(1, 150) == 1:
        rock_x = randint(0, 640 - rock.get_width())
        rock_y = 0 - rock.get_height()
        rocks.append((rock_x, rock_y))

    window.fill((0, 0, 0))

    # meteor shower
    for i, (rock_x, rock_y) in enumerate(rocks):
        rock_y += 1
        rocks[i] = (rock_x, rock_y)

        # measurement for colision
        robot_rect = robot.get_rect(topleft=(x, y))
        rock_rect = rock.get_rect(topleft=(rock_x, rock_y))

        # check for colision
        if robot_rect.colliderect(rock_rect):
            del rocks[i]
            score += 1
        # elif rock hits bottom, end game
        elif rock_y >= 480 - rock.get_height():
            game_over = font.render("Game Over", True, (255, 0, 0))
            x = 0
            y = 480 - robot.get_height()
            window.blit(game_over, (640 // 2 - game_over.get_width() // 2, 480 // 2))            
            break

    # draw items (meteors within loop)
        window.blit(rock, (rock_x, rock_y))          
    window.blit(robot, (x, y))
    text = font.render(f"Score: {score}", True, (255, 0, 0))    
    window.blit(text, (500, 10))
    
    pygame.display.flip()

    clock.tick(60)