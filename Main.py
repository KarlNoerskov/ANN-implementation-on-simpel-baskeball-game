import sys
import pygame
from Objects.Basketball import Basketball
from Objects.Hoop import Hoop
from GameManager import GameManager
from ANN import ANN
import random

# Initialization
pygame.init()

# Screen Setup
WIDTH = 800
HEIGHT = 600
Screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ANN Basketball")

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)

# Fonts
my_font = pygame.font.SysFont(None, 48)

# Time and Framerate
clock = pygame.time.Clock()

# Game Objects
hoop1 = Hoop(700, 200)



gamemanager1 = GameManager(hoop1, WIDTH, HEIGHT)
gamemanager1.createFirstGen()



# Game State Variables
shotCharging = False
shotPower = 0
running = True
hasShot = True

# Main Game Loop
while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                hasShot = True
                gamemanager1.reset()
                shotCharging = False
                shotPower = 0

    # 2. Logic Update
    for ball in gamemanager1.balls:
        ball.update(HEIGHT, WIDTH)
    for ann in gamemanager1.anns:
        ann.update()
    gamemanager1.update()

    
    # 3. Rendering
    Screen.fill(WHITE)
    for ball in gamemanager1.balls:
        ball.draw(Screen)
    hoop1.draw(Screen)
    
    score_text = my_font.render(f"Score: {gamemanager1.score}", True, BLACK)
    Screen.blit(score_text, (20, 10))
    fitnessscore = my_font.render(f"Score: {ann.fitnessScore}", True, BLACK)
    Screen.blit(fitnessscore, (400, 10))
    generation = my_font.render(f"Gen: {gamemanager1.generation}", True, BLACK)
    Screen.blit(generation, (200, 10))
    
    pygame.display.flip()
    clock.tick(240)


pygame.quit()
sys.exit()