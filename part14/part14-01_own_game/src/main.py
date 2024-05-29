# Complete your game here
import pygame
from random import randint

# basic settings as CONSTANTS
WIDTH, HEIGHT = 800, 600
SPEED = 3
DIFFICULTY = 5
HEALTH = 3
COINS = 10

class GameProject:
    def __init__(self) -> None:
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.game_font = pygame.font.SysFont("Courier", 24)
        pygame.display.set_caption("Cursed Coins")

        self.load_assets()
        self.instructions()
        self.new_game()
        self.main_loop()
    
    def instructions(self):
        # display game instruction
        instructions = [
            "Welcome to Cursed Coins",
            "Use the arrow keys to move the robot",
            f"Collect all {COINS} coins and find the exit",
            "don't let the ghosts get your soul",
            "Press any key to start the game"
            ]
        
        self.window.fill((0, 0, 0))
        for i, instruction in enumerate(instructions):
            text = self.game_font.render(instruction, True, (255, 0, 0))
            self.window.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - len(instructions) * text.get_height() // 2 + i * text.get_height()))
        pygame.display.flip()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    return

    def load_assets(self):
        # load all images
        self.robot = pygame.image.load("robot.png")
        self.ghost = pygame.image.load("monster.png")
        self.coin = pygame.image.load("coin.png")
        self.door = pygame.image.load("door.png")

    def new_game(self):
        # reset all game elements and positions 
        self.winner = False
        self.game_over = False
        self.health = HEALTH
        self.coins = 0
        self.robot_x = 0
        self.robot_y = HEIGHT - self.robot.get_height()
        self.robot_rect = self.robot.get_rect(topleft=(self.robot_x, self.robot_y))

        self.ghost_rects = []
        self.coin_rect = None
        self.door_rect = None
        self.door_x, self.door_y = None, None

        self.coin_x, self.coin_y = self.random_position(self.coin)
        self.coin_rect = self.coin.get_rect(topleft=(self.coin_x, self.coin_y))

        self.set_ghosts()

    def set_ghosts(self):
        # set ghost posotions
        self.ghost_positions = [self.random_position(self.ghost) for _ in range(DIFFICULTY)]
        self.ghost_rects = [self.ghost.get_rect(topleft=pos) for pos in self.ghost_positions]       

    def random_position(self, image):
        # randomize positions and don't directly overlap images
        buffer = 50
        while True:
            pos = [randint(0, WIDTH-image.get_width()), randint(0, HEIGHT-image.get_height())]
            if abs(self.robot_x - pos[0]) > buffer and abs(self.robot_y - pos[1]) > buffer:
                image_rect = image.get_rect(topleft=pos)
                if not any(image_rect.colliderect(ghost_rect.inflate(buffer, buffer)) for ghost_rect in self.ghost_rects) and \
                (self.coin_rect is None or not image_rect.colliderect(self.coin_rect)) and \
                (self.door_rect is None or not image_rect.colliderect(self.door_rect)):
                    return pos
    
    def game_status(self):
        if self.coins < COINS:
            self.collect_coins()
        else:
            self.create_exit()
        self.check_game_over()

    def collect_coins(self):
        # if coin collected, create a new coin
        if self.robot_rect.colliderect(self.coin_rect):
            self.coins += 1
            self.coin_x, self.coin_y = self.random_position(self.coin)
            self.coin_rect.topleft = (self.coin_x, self.coin_y)
            self.set_ghosts()

    def create_exit(self):
        # Door placement and removing coin after collecting coins
        if self.door_x is None and self.door_y is None and self.coins == COINS:
            self.coin_x, self.coin_y = None, None
            self.coin_rect = None
            self.door_x, self.door_y = self.random_position(self.door)
            self.door_rect = self.door.get_rect(topleft=(self.door_x, self.door_y))
    
    def check_game_over(self):
        # check if exit found
        if self.door_rect and self.robot_rect.colliderect(self.door_rect):
            self.winner = True                
            self.game_over = True
    
        # Ghost collision check
        for ghost_rect in self.ghost_rects:
            if self.robot_rect.colliderect(ghost_rect):
                self.health -= 1
                if self.health > 0:                    
                    self.set_ghosts()
                    self.window.fill((255, 0, 0))
                    pygame.display.flip()
                    pygame.time.wait(20)
                else:
                    self.game_over = True        

    def main_loop(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            keys = pygame.key.get_pressed()        
            if not self.game_over:
                # movement with arrow keys                
                if keys[pygame.K_LEFT] and self.robot_x > 0:
                    self.robot_x -= SPEED
                if keys[pygame.K_RIGHT] and self.robot_x < WIDTH - self.robot.get_width():
                    self.robot_x += SPEED
                if keys[pygame.K_UP] and self.robot_y > 0:
                    self.robot_y -= SPEED
                if keys[pygame.K_DOWN] and self.robot_y < HEIGHT - self.robot.get_height():
                    self.robot_y += SPEED
                self.robot_rect.topleft = (self.robot_x, self.robot_y)
            else:
                if keys[pygame.K_F2]:
                    self.new_game()
                if keys[pygame.K_ESCAPE]:
                    exit()                   
                
            self.game_status()
            self.draw_window()            
            clock.tick(60)
    
    def draw_window(self):
        # draw all elements on screen
        self.window.fill((0, 0, 0))

        if self.game_over:
            if self.winner:
                game_text_1 = self.game_font.render("Congratulations!", True, (255, 0, 0))
                game_text_2 = self.game_font.render("You collected the coins and found the exit!", True, (255, 0, 0))
            else:
                game_text_1 = self.game_font.render("The ghosts got your soul!", True, (255, 0, 0))
                game_text_2 = self.game_font.render("Game Over", True, (255, 0, 0))
            self.window.blit(game_text_1, (WIDTH // 2 - game_text_1.get_width() // 2, HEIGHT // 2 - game_text_1.get_height() * 2))
            self.window.blit(game_text_2, (WIDTH // 2 - game_text_2.get_width() // 2, HEIGHT // 2 - game_text_1.get_height()))
            exit_text = self.game_font.render("F2 = New Game  -  esc = Exit", True, (255, 0, 0))
            self.window.blit(exit_text, (WIDTH // 2 - exit_text.get_width() // 2, HEIGHT // 2 + game_text_1.get_height()))
        else:    
            self.window.blit(self.robot, (self.robot_x, self.robot_y))
            for pos in self.ghost_positions:
                # self.ghost.fill((255, 255, 255))
                self.window.blit(self.ghost, (pos))
            if self.coin_rect is not None:
                self.window.blit(self.coin, (self.coin_x, self.coin_y))
            if self.door_rect is not None:
                self.window.blit(self.door, (self.door_x, self.door_y))
        score_text = self.game_font.render(f"Coins: {self.coins}", True, (255, 0, 0))
        self.window.blit(score_text, (10, 10))
        health_text = self.game_font.render(f"Health: {self.health * "*"}", True, (255, 0, 0))
        self.window.blit(health_text, (600, 10))
        pygame.display.flip()

if __name__ == "__main__":
    GameProject()